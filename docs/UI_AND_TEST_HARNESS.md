---
tags: [ui, dashboard, tkinter, test_harness, threads]
aliases: [UI and Test Harness, Desktop Dashboard, Tkinter Interface]
---

# 🖥️ Tkinter UI & Test Harness Architecture

This document details the graphical presentation tier of SYNAPSE MOCK SERVER. It explains the **`MockApp`** Tkinter dashboard, thread decoupling, map validation, and asynchronous console logging.

⬅️ Back to [Main Documentation Hub](SYNAPSE_MOCK_MOC.md) | 🏛️ See [Architecture](ARCHITECTURE.md) | ⚡ See [API Reference](API_REFERENCE.md)

---

## 1. Interface Layout & Component Hierarchy

The desktop interface (`ui/app_ui.py`) provides operators with a simple, high-visibility control console:

```mermaid
graph TD
    Root[Tkinter Root Window - 600x400]
    Header[Header Title Bar]
    MapFrame[Map Selection LabelFrame]
    Controls[Control Panel Frame]
    LogFrame[System Logs LabelFrame]
    StatusBar[Status Bar]

    Root --> Header
    Root --> MapFrame
    Root --> Controls
    Root --> LogFrame
    Root --> StatusBar

    MapFrame --> FilePath[Selected File Label]
    MapFrame --> FileBtn[Select .net.xml.gz Button]

    Controls --> PlayBtn[▶ Play Button #28a745]
    Controls --> StopBtn[Stop Button]

    LogFrame --> TextConsole[Dark Text Area #1e1e1e]
    LogFrame --> Scrollbar[Vertical Scrollbar]
```

### 1.1 Visual Elements Breakdown
- **Map Selection Panel:** Displays the active road network path and opens the OS file picker.
- **Controls Panel:**
  - `▶ Play` button: Triggers parsing, spawns the background worker, and locks UI controls.
  - `Stop` button: Signals the streaming loop to stop and resets controls.
- **Dark Console (`#1e1e1e`):** Fixed-width console (`Consolas`, 9pt) outputting timestamped transmission events.
- **Status Bar:** Bottom banner showing connection and operational states.

---

## 2. Multi-Threaded Execution Model

Network streaming and file decompression must not execute on the Tkinter main thread, as doing so freezes the GUI.

```mermaid
sequenceDiagram
    autonumber
    actor Operator
    participant UI as Tkinter Main Thread
    participant Worker as Background Daemon Thread
    participant Client as GRPCClient
    participant Server as Remote HFTLink Server

    Operator->>UI: Select map & Click "▶ Play"
    UI->>UI: Parse edge IDs from map
    UI->>Worker: threading.Thread(target=_run_simulation, daemon=True).start()
    UI->>UI: Update status: "Connecting..."
    
    Worker->>Client: connect("localhost:50051")
    Worker->>Client: load_scenario(map_path)
    Client->>Server: LoadScenario
    Server-->>Client: ScenarioStatus(accepted=True)
    
    Worker->>Client: system_control("START")
    Client->>Server: SystemControl(START)
    Server-->>Client: CommandResponse(success=True)

    loop High-Frequency Stream (10-20 Hz)
        Worker->>Client: stream_traffic(...)
        Worker->>UI: root.after(0, _update_log)
        UI->>UI: Append log line to console
    end
```

### 2.1 Thread-Safe Log Dispatch (`root.after`)
Tkinter requires that all widget modifications happen strictly on the main thread:

```python
def log(self, message):
    timestamp = time.strftime("%H:%M:%S")
    full_message = f"[{timestamp}] {message}\n"
    print(full_message.strip())
    
    def _update():
        self.log_area.config(state="normal")
        self.log_area.insert(tk.END, full_message)
        self.log_area.see(tk.END)
        self.log_area.config(state="disabled")
    
    # Safely schedule widget update onto Tkinter event loop
    self.root.after(0, _update)
```

---

## 3. Resilient Auto-Reconnection

If the gRPC connection to the server drops during streaming, `_run_simulation` captures the exception and enters an automated reconnection loop:

1. Logs the disconnect event: `CONNECTION LOST: <reason>`.
2. Updates UI status: `Status: Connection lost. Retrying...`.
3. Pauses for 3 seconds.
4. Attempts re-connection and scenario reloading automatically until stopped by the user.

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>UI & Test Harness Guide • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
