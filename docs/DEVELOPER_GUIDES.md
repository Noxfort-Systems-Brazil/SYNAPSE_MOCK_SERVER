---
tags: [developer, guide, setup, proto, generators]
aliases: [Developer Guides, Integration Guide, Extending Generators]
---

# 🛠️ Developer & Integration Guides

This document provides step-by-step guidance for developers wishing to extend, customize, or integrate with **SYNAPSE MOCK SERVER**.

⬅️ Back to [Main Documentation Hub](SYNAPSE_MOCK_MOC.md) | 🏛️ See [Architecture](ARCHITECTURE.md) | ⚡ See [API Reference](API_REFERENCE.md)

---

## 1. Local Environment Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Noxfort-Systems-Brazil/Synapse_Mock_Server.git
   cd Synapse_Mock_Server
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 2. Compiling Protocol Buffers

If you make modifications to `proto/synapse_hft.proto`, recompile the Python gRPC stubs:

```bash
python -m grpc_tools.protoc \
    -I. \
    --python_out=. \
    --grpc_python_out=. \
    proto/synapse_hft.proto
```

This updates:
- `proto/synapse_hft_pb2.py`
- `proto/synapse_hft_pb2_grpc.py`

---

## 3. Creating a Custom Traffic Generator

To implement a new traffic generation model (e.g., an incident spike generator):

1. **Implement `IDataGenerator`:**
   ```python
   # infrastructure/custom_generator.py
   import time
   from interfaces import IDataGenerator

   class CustomIncidentGenerator(IDataGenerator):
       def __init__(self, edge_ids=None):
           self.edge_ids = edge_ids or []

       def set_edges(self, edge_ids):
           self.edge_ids = edge_ids

       def generate_frame(self, sequence_id: int):
           return {
               "timestamp": time.time(),
               "sequence_id": sequence_id,
               "edges": {
                   eid: {
                       "occupancy": 0.95,
                       "mean_speed": 5.0,
                       "queue_length": 120,
                       "density": 140.0
                   }
                   for eid in self.edge_ids
               }
           }
   ```

2. **Inject into `main.py`:**
   ```python
   # main.py
   from infrastructure.custom_generator import CustomIncidentGenerator

   def main():
       root = tk.Tk()
       client = GRPCClient()
       generator = CustomIncidentGenerator()
       app = MockApp(root, client, generator)
       root.mainloop()
   ```

---

## 4. Adding a New Network Parser (OCP)

To support another network format (e.g., GeoJSON):

1. Implement `FileParser` from `interfaces/parser_interface.py`:
   ```python
   from interfaces.parser_interface import FileParser

   class GeoJSONParser(FileParser):
       def parse_file(self, file_path: str):
           # Parse and return dictionary
           pass
   ```

2. Inject it into `TopologyAnalyzer`:
   ```python
   analyzer = TopologyAnalyzer(parser=GeoJSONParser())
   ```

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Developer Guides • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
