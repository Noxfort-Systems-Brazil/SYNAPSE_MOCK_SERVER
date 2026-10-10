---
tags: [topology, sumo, network, graph, solid, xml]
aliases: [Topology Analysis, SUMO Network Extraction, SOLID Parser]
---

# 🗺️ Topology Analysis Engine & SUMO Parsers

This document provides a comprehensive guide to the **Topology Analysis Engine** in SYNAPSE MOCK SERVER. It explains the parsing of SUMO `.net.xml` networks, the modular SOLID architecture, graph data structures, and directional querying algorithms.

⬅️ Back to [Main Documentation Hub](synapse_mock_moc.md) | 🏛️ See [Architecture](architecture.md) | ⚡ See [API Reference](api_reference.md)

---

## 1. Overview & Network Topology in SUMO

In microscopic traffic simulation environments (such as SUMO), road networks are defined as directed graphs composed of:
- **Junctions (Nodes):** Intersections where streets connect. Controlled junctions include traffic signal logic (`type="traffic_light"`).
- **Edges (Links):** Directional roadway links between junctions. Edges contain one or more parallel lanes.
- **Connections:** Explicit lane-to-lane directional links governing turn movements.
- **Internal Edges:** Intermediate connector edges within junctions, indicated by a `:` prefix. These are automatically filtered out during edge extraction.

---

## 2. SOLID Architecture Breakdown

To guarantee high testability and maintainability, the topology subsystem is segregated into modular components adhering to **SOLID**:

```mermaid
classDiagram
    class FileParser {
        <<interface>>
        +parse_file(file_path: str) Any
    }

    class XMLParser {
        +parse_file(file_path: str) ElementTree
    }

    class TopologyExtractor {
        <<interface>>
        +extract_junctions(data) Dict
        +extract_edges(data) Dict
        +extract_connections(data) List
    }

    class TopologyExtractorImpl {
        +extract_junctions(data) Dict
        +extract_edges(data) Dict
        +extract_connections(data) List
    }

    class TopologyQuerier {
        <<interface>>
        +get_downstream_edges(edge_id, edges, junctions) List
        +get_upstream_edges(edge_id, edges, junctions) List
    }

    class TopologyQuerierImpl {
        +get_downstream_edges(edge_id, edges, junctions) List
        +get_upstream_edges(edge_id, edges, junctions) List
    }

    class TopologyReporter {
        <<interface>>
        +print_topology_summary(edges, junctions, connections)
    }

    class TopologyReporterImpl {
        +print_topology_summary(edges, junctions, connections)
    }

    class TopologyAnalyzer {
        -parser: FileParser
        -extractor: TopologyExtractor
        -querier: TopologyQuerier
        -reporter: TopologyReporter
        +analyze_file(file_path: str) bool
        +get_downstream_edges(edge_id: str) List
        +get_upstream_edges(edge_id: str) List
        +get_connected_edges(edge_id: str) Dict
        +print_topology_summary()
    }

    FileParser <|.. XMLParser
    TopologyExtractor <|.. TopologyExtractorImpl
    TopologyQuerier <|.. TopologyQuerierImpl
    TopologyReporter <|.. TopologyReporterImpl

    TopologyAnalyzer o-- FileParser
    TopologyAnalyzer o-- TopologyExtractor
    TopologyAnalyzer o-- TopologyQuerier
    TopologyAnalyzer o-- TopologyReporter
```

---

## 3. Directional Adjacency Querying

```python
from infrastructure.topology_analyzer import TopologyAnalyzer

analyzer = TopologyAnalyzer()
if analyzer.analyze_file("data/maps/sample.net.xml.gz"):
    analyzer.print_topology_summary()
    downstream = analyzer.get_downstream_edges("edge_main_avenue")
    upstream = analyzer.get_upstream_edges("edge_main_avenue")
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Topology Analysis Guide • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
