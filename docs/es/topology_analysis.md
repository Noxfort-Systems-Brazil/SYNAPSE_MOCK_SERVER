---
tags: [topology, sumo, network, graph, solid, xml]
aliases: [Análisis Topológico, Redes SUMO, Parser SOLID]
---

# 🗺️ Análisis de Topología Vial & Parsers SUMO

Este documento describe el subsistema de análisis topológico en SYNAPSE MOCK SERVER, abordando el procesamiento de redes SUMO (`.net.xml`), clases de datos y consultas direccionales en el grafo.

⬅️ Volver al [Centro de Documentación](README.md) | 🏛️ Ver [Arquitectura](architecture.md) | ⚡ Ver [API](api_reference.md)

---

## 1. Topología en Redes SUMO

Las redes viales representan la ciudad como un grafo dirigido:
- **Intersecciones (`junction`):** Nodos de convergencia vial.
- **Tramos Viales (`edge`):** Enlaces unidireccionales que alojan carriles (`lane`).
- **Conexiones (`connection`):** Enlaces entre carriles para giros permitidos.
- **Aristas Internas:** Vías temporales internas dentro de los cruces (prefijo `:`), descartadas automáticamente.

---

## 2. Consultas Direccionales en Grafo

```python
from infrastructure.topology_analyzer import TopologyAnalyzer

analyzer = TopologyAnalyzer()
if analyzer.analyze_file("ruta/al/mapa.net.xml.gz"):
    downstream = analyzer.get_downstream_edges("via_principal")
    upstream = analyzer.get_upstream_edges("via_principal")
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Análisis Topológico</i>
</div>
