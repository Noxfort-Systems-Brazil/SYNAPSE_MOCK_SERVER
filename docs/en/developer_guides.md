---
tags: [developer, guide, setup, proto, generators]
aliases: [Developer Guides, Integration Guide, Extending Generators]
---

# 🛠️ Developer & Integration Guides

This document provides step-by-step guidance for developers wishing to extend, customize, or integrate with **SYNAPSE MOCK SERVER**.

⬅️ Back to [Main Documentation Hub](synapse_mock_moc.md) | 🏛️ See [Architecture](architecture.md) | ⚡ See [API Reference](api_reference.md)

---

## 1. Local Environment Setup

```bash
git clone https://github.com/Noxfort-Systems-Brazil/Synapse_Mock_Server.git
cd Synapse_Mock_Server

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 2. Compiling Protocol Buffers

```bash
python -m grpc_tools.protoc \
    -I. \
    --python_out=. \
    --grpc_python_out=. \
    proto/synapse_hft.proto
```

---

## 3. Creating a Custom Traffic Generator

```python
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

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Developer Guides • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
