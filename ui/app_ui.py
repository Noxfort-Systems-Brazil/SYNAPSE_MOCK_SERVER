# Synapse Mock Server is an open-source test harness and telemetry simulator for the Synapse HFT protocol.
# Copyright (C) 2026 Gabriel Moraes - Noxfort Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# File: ui/app_ui.py
# Author: Gabriel Moraes
# Date: October 2026

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
import os
from infrastructure.parser import extract_edge_ids

class MockApp:
    def __init__(self, root, client, generator):
        self.root = root
        self.root.title("Synapse Mock Server (HFTLink)")
        self.root.geometry("600x400")
        
        self.client = client
        self.generator = generator
        
        self.selected_file = tk.StringVar(value="No file selected")
        self.is_running = False
        self.thread = None
        self.frame_count = 0
        
        self._setup_ui()
        
    def _setup_ui(self):
        # Header
        header = tk.Label(self.root, text="Synapse Mock Server", font=("Helvetica", 16, "bold"))
        header.pack(pady=10)
        
        # File Selection Frame
        file_frame = tk.LabelFrame(self.root, text="Map Selection", padx=10, pady=10)
        file_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(file_frame, textvariable=self.selected_file, wraplength=400).pack(side="left", padx=5)
        tk.Button(file_frame, text="Select .net.xml.gz", command=self._select_file).pack(side="right")
        
        # Controls
        ctrl_frame = tk.Frame(self.root)
        ctrl_frame.pack(pady=40)
        
        self.start_btn = tk.Button(ctrl_frame, text="▶ Play", command=self._start_sim, width=15, bg="#28a745", fg="white", font=("Helvetica", 10, "bold"))
        self.start_btn.pack(side="left", padx=5)
        
        self.stop_btn = tk.Button(ctrl_frame, text="Stop", command=self._stop_sim, width=15, state="disabled")
        self.stop_btn.pack(side="left", padx=5)
        
        # Log Console
        log_frame = tk.LabelFrame(self.root, text="System Logs", padx=5, pady=5)
        log_frame.pack(fill="both", expand=True, padx=20, pady=5)
        
        self.log_area = tk.Text(log_frame, height=8, font=("Consolas", 9), state="disabled", bg="#1e1e1e", fg="#d4d4d4")
        self.log_area.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(log_frame, command=self.log_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_area.config(yscrollcommand=scrollbar.set)
        
        # Status
        self.status_var = tk.StringVar(value="Status: Ready")
        self.status_label = tk.Label(self.root, textvariable=self.status_var, bd=1, relief="sunken", anchor="w")
        self.status_label.pack(side="bottom", fill="x")

    def _select_file(self):
        filename = filedialog.askopenfilename(
            title="Select compressed SUMO Map file",
            filetypes=(("SUMO Network GZ", "*.net.xml.gz"), ("All files", "*.*"))
        )
        if filename:
            if not filename.endswith('.net.xml.gz'):
                messagebox.showwarning("Invalid File", "Please select a file ending in .net.xml.gz")
                return
            self.selected_file.set(filename)
            self.log(f"Map selected: {os.path.basename(filename)}")

    def log(self, message):
        """Thread-safe logging to the UI console and terminal."""
        timestamp = time.strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        print(full_message.strip())
        
        def _update():
            self.log_area.config(state="normal")
            self.log_area.insert(tk.END, full_message)
            self.log_area.see(tk.END)
            self.log_area.config(state="disabled")
        
        self.root.after(0, _update)

    def _start_sim(self):
        if self.selected_file.get() == "No file selected" or not os.path.exists(self.selected_file.get()):
            messagebox.showwarning("Warning", "Map file not ready. Please select a valid .xml file before playing.")
            return
            
        self.is_running = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        
        # Parse map to extract edges
        try:
            edges = extract_edge_ids(self.selected_file.get())
            if edges:
                self.generator.set_edges(edges)
                self.status_var.set(f"Status: Loaded {len(edges)} edges. Connecting...")
            else:
                self.status_var.set("Warning: No edges found in map. Using defaults.")
        except Exception as e:
            messagebox.showerror("Parser Error", f"Failed to parse map: {e}")
            self._reset_ui()
            return

        self.status_var.set("Status: Connecting to Carina...")
        
        self.thread = threading.Thread(target=self._run_simulation, daemon=True)
        self.thread.start()

    def _stop_sim(self):
        self.is_running = False
        self.client.stop_streaming()
        self.status_var.set("Status: Stopping...")

    def _run_simulation(self):
        self.frame_count = 0
        while self.is_running:
            try:
                self.log(f"Attempting to connect to Carina at localhost:50051...")
                self.status_var.set("Status: Attempting to connect...")
                self.client.connect("localhost:50051")
                
                # Try to load scenario
                success = self.client.load_scenario(self.selected_file.get())
                if not success:
                    self.log("ERROR: Carina rejected map file.")
                    self.status_var.set("Status: Map rejected. Retrying...")
                    time.sleep(5)
                    continue
                    
                self.log("SUCCESS: Connected and Scenario Loaded.")
                self.status_var.set("Status: Unlocking System (START)...")
                
                # Mandatory SystemControl START
                if self.client.system_control("START"):
                    self.log("SUCCESS: System Unlocked (START accepted).")
                    self.status_var.set("Status: Connected! Streaming...")
                else:
                    self.log("WARNING: SystemControl START failed or rejected.")
                    self.status_var.set("Status: System Locked. Still trying to stream...")
                
                # Stream
                def on_frame_sent(seq_id, frame):
                    self.frame_count += 1
                    if self.frame_count % 10 == 0: # Log every 10 frames to avoid spam
                        edge_count = len(frame.edges)
                        sample_info = ""
                        if edge_count > 0:
                            first_edge = list(frame.edges.keys())[0]
                            state = frame.edges[first_edge]
                            sample_info = f" | Sample: {first_edge} (Occ: {state.occupancy:.2f}, Spd: {state.mean_speed:.2f})"
                        
                        self.log(f"SENT [ID:{seq_id}] {edge_count} edges{sample_info}")
                
                self.client.stream_traffic(self.generator, on_frame_sent=on_frame_sent)
                
            except Exception as e:
                if self.is_running:
                    self.log(f"CONNECTION LOST: {str(e)}")
                    self.status_var.set("Status: Connection lost. Retrying...")
                    time.sleep(3)
                else:
                    break
        
        self.log("Simulation Stopped.")
        self._reset_ui()

    def _reset_ui(self):
        self.is_running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status_var.set("Status: Stopped")
