---
tags: [developer, guide, setup, proto, generators]
aliases: [Guias do Desenvolvedor, Setup, Novos Geradores]
---

# 🛠️ Guias do Desenvolvedor & Extensão

Este documento orienta os desenvolvedores no setup do ambiente local, recompilação dos contratos gRPC e criação de novos módulos.

⬅️ Voltar para o [Hub de Documentação](synapse_mock_moc.md) | 🏛️ Ver [Arquitetura](architecture.md) | ⚡ Ver [API](api_reference.md)

---

## 1. Configuração do Ambiente

```bash
git clone https://github.com/Noxfort-Systems-Brazil/Synapse_Mock_Server.git
cd Synapse_Mock_Server

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 2. Recompilando Protocol Buffers

Caso altere o arquivo `proto/synapse_hft.proto`, gere novamente os módulos Python:

```bash
python -m grpc_tools.protoc \
    -I. \
    --python_out=. \
    --grpc_python_out=. \
    proto/synapse_hft.proto
```

---

## 3. Criando um Novo Gerador de Tráfego

Basta implementar a interface `IDataGenerator` (`interfaces.py`):

```python
import time
from interfaces import IDataGenerator

class MeuGeradorPersonalizado(IDataGenerator):
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
                    "occupancy": 0.5,
                    "mean_speed": 50.0,
                    "queue_length": 5,
                    "density": 30.0
                }
                for eid in self.edge_ids
            }
        }
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Guias do Desenvolvedor</i>
</div>
