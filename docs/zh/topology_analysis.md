---
tags: [topology, sumo, network, graph, solid, xml]
aliases: [拓扑分析, SUMO 路网解析]
---

# 🗺️ 拓扑分析引擎与 SUMO 路网解析

本文档介绍 SYNAPSE MOCK SERVER 的 SUMO 路网拓扑分析与图遍历查询引擎。

⬅️ 返回 [文档中心](README.md) | 🏛️ 查看 [系统架构](architecture.md)

---

## 1. 邻接与上下游查询示例

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
  <i>SYNAPSE MOCK SERVER v1.2.0 • 拓扑分析</i>
</div>
