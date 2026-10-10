---
tags: [moc, hub, docs, obsidian, synapse, mock_server, index]
aliases: [Synapse Mock MOC, Master Documentation Hub, Documentation Index, Knowledge Vault]
---

<div align="center">

<img src="assets/synapse-logo.png" alt="SYNAPSE MOCK SERVER Logo" width="120" />

# SYNAPSE MOCK SERVER Technical Master Documentation Hub
### Central Index & Client Architecture Knowledge Vault
*Noxfort Systems — A State Of Art Company*

</div>

Welcome to the **SYNAPSE MOCK SERVER** technical documentation library. Designed as a high-frequency test harness and telemetry load simulator for the Synapse wire protocol, this engine stresses, verifies, and benchmarks real-time intelligent traffic light controllers, digital twins, and gRPC servers in the CARINA ecosystem.

This master documentation index provides deep technical coverage for developers, traffic systems engineers, and QA automation teams. It is fully compatible with both **GitHub** and **[Obsidian](https://obsidian.md/)**.

---

## 🗺️ Codebase Map & Directory Hierarchy

```text
Synapse_Mock_Server/
├── main.py                     # Desktop UI Application Entrypoint
├── ARCHITECTURE.md             # Clean Architecture Blueprint, SOLID & Thread Model
├── CHANGELOG.md                # Semantic versioning release history
├── CONTRIBUTING.md             # Developer contribution guidelines
├── CODE_OF_CONDUCT.md         # Contributor Covenant standard
├── SECURITY.md                 # Vulnerability reporting protocol
├── LICENSE                     # Apache License 2.0
├── requirements.txt            # Python dependencies (grpcio, protobuf, tkinter)
├── run.sh                      # Posix runner with virtualenv detection
├── peak_schedule.json          # ADAGIO offline peak schedule payload
├── SOLID_IMPROVEMENTS.md       # Refactoring log & architectural decisions
├── simple_test.py              # Quick integration test harness
├── test_topology_analyzer.py   # Topology extraction & query unit tests
│
├── interfaces/                 # SOLID Domain Interface Contracts
│   ├── parser_interface.py     # FileParser abstract base class
│   └── topology_interface.py   # TopologyExtractor, TopologyQuerier, TopologyReporter
├── interfaces.py               # Top-level client & generator interfaces (IDataGenerator, ISynapseClient)
│
├── infrastructure/             # Concrete Infrastructure & Implementations
│   ├── grpc_client.py          # gRPC client stub implementing ISynapseClient
│   ├── generator.py            # RandomTrafficGenerator (random walk)
│   ├── realistic_generator.py  # RealisticTrafficGenerator (diurnal curves + 4 states)
│   ├── parser.py               # Fast extract_edge_ids helper (.xml & .gz)
│   ├── topology_analyzer.py    # Facade coordinator with Dependency Injection
│   ├── parsers/                # Parser implementations
│   │   └── xml_parser.py       # XMLParser conforming to FileParser
│   └── topology/               # Topology analysis components
│       ├── topology_extractor.py # EdgeInfo, JunctionInfo, ConnectionInfo extractor
│       ├── topology_querier.py   # Upstream/downstream relationship querier
│       └── topology_reporter.py  # Formatted console summary reporter
│
├── proto/                      # gRPC Protocol Specifications
│   ├── synapse_hft.proto       # Service & message definitions (HFTLink)
│   ├── synapse_hft_pb2.py      # Compiled Protobuf classes
│   └── synapse_hft_pb2_grpc.py # Compiled gRPC stubs
│
├── ui/                         # Presentation Layer
│   └── app_ui.py               # MockApp Tkinter dark desktop dashboard
│
└── docs/                       # Comprehensive Knowledge Vault & Documentation
    ├── README.md               # Central Documentation Hub & Language matrix
    ├── index.md                # MkDocs Entry Point & Portal
    ├── SYNAPSE_MOCK_MOC.md     # Master Map of Content (This Document)
    ├── ARCHITECTURE.md         # Clean Architecture & Concurrency Blueprint
    ├── API_REFERENCE.md        # Synapse HFT gRPC Protocol & Frame Specifications
    ├── TOPOLOGY_ANALYSIS.md    # SUMO Road Network Extraction & SOLID Parsers
    ├── TRAFFIC_SIMULATION.md   # Diurnal Traffic Models & 4 Congestion Regimes
    ├── UI_AND_TEST_HARNESS.md  # Desktop Dashboard, Worker Threading & Status Logging
    ├── TESTING.md              # Test Suite & Verification Guidelines
    ├── DEVELOPER_GUIDES.md     # Protoc Compilation & Generator Extension
    ├── DEPLOYMENT_AND_PACKAGING.md # Shell Runner, Virtualenvs & Automation
    ├── stylesheets/            # Custom Material for MkDocs CSS
    ├── assets/                 # Brand logos (CARINA, Noxfort)
    ├── pt-br/                  # Portuguese (Brazil) documentation
    ├── en/                     # English canonical documentation
    ├── es/                     # Spanish documentation
    ├── fr/                     # French documentation
    ├── ru/                     # Russian documentation
    └── zh/                     # Simplified Chinese documentation
```

---

## 🎯 Master Topic Navigation

- **Core Architecture & SOLID Blueprint:** [`ARCHITECTURE.md`](ARCHITECTURE.md)
- **Synapse HFT gRPC API Reference:** [`API_REFERENCE.md`](API_REFERENCE.md)
- **Topology Analysis & SUMO Network Parsers:** [`TOPOLOGY_ANALYSIS.md`](TOPOLOGY_ANALYSIS.md)
- **Traffic Simulation Mechanics & Formulations:** [`TRAFFIC_SIMULATION.md`](TRAFFIC_SIMULATION.md)
- **Tkinter Desktop UI & Test Harness:** [`UI_AND_TEST_HARNESS.md`](UI_AND_TEST_HARNESS.md)
- **Testing, Verification & Quality Assurance:** [`TESTING.md`](TESTING.md)
- **Developer & Integration Guides:** [`DEVELOPER_GUIDES.md`](DEVELOPER_GUIDES.md)
- **Deployment, Shell Runner & Environments:** [`DEPLOYMENT_AND_PACKAGING.md`](DEPLOYMENT_AND_PACKAGING.md)

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Master Map of Content • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
