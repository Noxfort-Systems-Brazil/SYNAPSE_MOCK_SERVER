---
tags: [topology, sumo, network, graph, solid, xml]
aliases: [Análise Topológica, Extração de Redes SUMO, Parser SOLID]
---

# 🗺️ Análise de Topologia Viária & Parsers SUMO

Este documento descreve o funcionamento do módulo de análise topológica viária do **SYNAPSE MOCK SERVER**, abordando o parsing de redes do SUMO (`.net.xml`), extração de dados e consultas direcionais de grafo.

⬅️ Voltar para o [Hub de Documentação](synapse_mock_moc.md) | 🏛️ Ver [Arquitetura](architecture.md) | ⚡ Ver [API](api_reference.md)

---

## 1. Estruturas de Redes no SUMO

As redes viárias do SUMO modelam a cidade como um grafo direcionado:
- **Junções (`junction`):** Vértices do grafo onde vias convergem ou divergem. Vértices com semáforos possuem `type="traffic_light"`.
- **Arestas (`edge`):** Segmentos de via entre dois nós. Podem conter múltiplas faixas (`lane`).
- **Conexões (`connection`):** Ligações que determinam quais manobras de conversão são permitidas entre faixas.
- **Arestas Internas:** Elementos intermediários gerados internamente pelo SUMO dentro dos cruzamentos (prefixo `:`). O analisador filtra e descarta essas arestas automaticamente.

---

## 2. Arquitetura Modular (SOLID)

O módulo foi estruturado em interfaces e implementações desacopladas:

- **`interfaces/parser_interface.py`:** Define a interface `FileParser`.
- **`interfaces/topology_interface.py`:** Define `TopologyExtractor`, `TopologyQuerier` e `TopologyReporter`.
- **`infrastructure/parsers/xml_parser.py`:** Implementação `XMLParser` compatível com arquivos `.xml` convencionais e compactados com gzip (`.xml.gz`).
- **`infrastructure/topology/topology_extractor.py`:** Implementação `TopologyExtractorImpl` que popula as dataclasses `EdgeInfo`, `JunctionInfo` e `ConnectionInfo`.
- **`infrastructure/topology/topology_querier.py`:** Implementação `TopologyQuerierImpl` com algoritmos de busca de arestas a montante e a jusante.
- **`infrastructure/topology/topology_reporter.py`:** Implementação `TopologyReporterImpl` para formatação de resumos executivos no terminal.
- **`infrastructure/topology_analyzer.py`:** Fachada coordenadora com injeção de dependências.

---

## 3. Consultas a Montante e a Jusante

As buscas de conectividade permitem navegar pelas vias vizinhas no grafo viário:

```python
from infrastructure.topology_analyzer import TopologyAnalyzer

analyzer = TopologyAnalyzer()
if analyzer.analyze_file("caminho/para/mapa.net.xml.gz"):
    # Consulta vias que recebem tráfego desta via (a jusante)
    downstream = analyzer.get_downstream_edges("via_avenida_brasil")
    
    # Consulta vias que alimentam esta via (a montante)
    upstream = analyzer.get_upstream_edges("via_avenida_brasil")
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Análise de Topologia</i>
</div>
