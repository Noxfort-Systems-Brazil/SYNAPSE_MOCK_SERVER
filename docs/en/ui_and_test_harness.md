---
tags: [ui, dashboard, tkinter, test_harness, threads]
aliases: [UI and Test Harness, Desktop Dashboard, Tkinter Interface]
---

# 🖥️ Tkinter UI & Test Harness Architecture

This document details the graphical presentation tier of SYNAPSE MOCK SERVER. It explains the **`MockApp`** Tkinter dashboard, thread decoupling, map validation, and asynchronous console logging.

⬅️ Back to [Main Documentation Hub](synapse_mock_moc.md) | 🏛️ See [Architecture](architecture.md) | ⚡ See [API Reference](api_reference.md)

---

## 1. Interface Layout & Component Hierarchy

The desktop interface (`ui/app_ui.py`) provides operators with a simple, high-visibility control console:

- **Map Selection Panel:** Displays the active road network path and opens the OS file picker.
- **Controls Panel:**
  - `▶ Play` button: Triggers parsing, spawns the background worker, and locks UI controls.
  - `Stop` button: Signals the streaming loop to stop and resets controls.
- **Dark Console (`#1e1e1e`):** Fixed-width console (`Consolas`, 9pt) outputting timestamped transmission events.
- **Status Bar:** Bottom banner showing connection and operational states.

---

## 2. Multi-Threaded Execution Model

Network streaming and file decompression do not execute on the Tkinter main thread to avoid GUI freezing:

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

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>UI & Test Harness Guide • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
