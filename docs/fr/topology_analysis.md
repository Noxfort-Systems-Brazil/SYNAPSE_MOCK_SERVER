---
tags: [topology, sumo, network, graph, solid, xml]
aliases: [Analyse Topologique, Réseaux SUMO]
---

# 🗺️ Analyse Topologique & Réseaux SUMO

Ce document décrit le module d'analyse topologique de réseaux SUMO (`.net.xml`) dans **SYNAPSE MOCK SERVER**.

⬅️ Retour au [Hub de Documentation](README.md) | 🏛️ Voir [Architecture](architecture.md)

---

## 1. Requêtes d'Adjacence

```python
from infrastructure.topology_analyzer import TopologyAnalyzer

analyzer = TopologyAnalyzer()
if analyzer.analyze_file("data/maps/sample.net.xml.gz"):
    downstream = analyzer.get_downstream_edges("edge_1")
    upstream = analyzer.get_upstream_edges("edge_1")
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Analyse Topologique</i>
</div>
