---
tags: [topology, sumo, network, graph, solid, xml]
aliases: [Топологический анализ, Сети SUMO]
---

# 🗺️ Топологический анализ & Дорожные сети SUMO

В этом документе описывается модуль анализа дорожных графов SUMO (`.net.xml`).

⬅️ Назад в [Центр документации](README.md) | 🏛️ См. [Архитектуру](architecture.md)

---

## 1. Запросы смежности графа

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
  <i>SYNAPSE MOCK SERVER v1.2.0 • Топологический анализ</i>
</div>
