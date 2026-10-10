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
# File: main.py
# Author: Gabriel Moraes
# Date: 2026-10-10

import tkinter as tk
from ui.app_ui import MockApp
from infrastructure.grpc_client import GRPCClient
from infrastructure.realistic_generator import RealisticTrafficGenerator

def main():
    root = tk.Tk()
    
    # Dependency Injection
    client = GRPCClient()
    generator = RealisticTrafficGenerator()
    
    # Initialize UI
    app = MockApp(root, client, generator)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nShutdown requested via Ctrl+C. Closing...")
        root.destroy()

if __name__ == "__main__":
    main()
