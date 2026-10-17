---
tags: [moc, hub, docs, obsidian, synapse, mock_server, index]
aliases: [Canonical Synapse Mock MOC, English MOC]
---

<div align="center">

# Master Map of Content (MOC) — SYNAPSE MOCK SERVER
### Canonical Technical Knowledge Vault
*Noxfort Systems — A State Of Art Company*

</div>

Welcome to the canonical technical documentation library for **SYNAPSE MOCK SERVER**. Designed as a high-frequency test harness and telemetry load simulator for the Synapse wire protocol, this engine stresses, verifies, and benchmarks real-time intelligent traffic light controllers, digital twins, and gRPC servers in the CARINA ecosystem.

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
├── LICENSE                     # Apache License 2.0 (SPDX: Apache-2.0)
├── pyproject.toml              # PEP 621/639 configuration (SPDX: Apache-2.0)
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
    ├── en/                     # Canonical English Documentation Suite
    │   ├── README.md           # English Hub
    │   ├── synapse_mock_moc.md # This Document
    │   ├── architecture.md     # Architecture & Concurrency
    │   ├── api_reference.md    # gRPC API Reference
    │   ├── topology_analysis.md# SUMO Topology Engine
    │   ├── traffic_simulation.md# Realistic Diurnal Dynamics
    │   ├── ui_and_test_harness.md# Tkinter Dashboard
    │   ├── testing.md          # Testing & QA
    │   ├── developer_guides.md # Developer Guides
    │   └── deployment_and_packaging.md # Deployment & Automation
    ├── pt-br/                  # Portuguese (Brazil) Documentation Suite
    ├── es/                     # Spanish Documentation Suite
    ├── fr/                     # French Documentation Suite
    ├── ru/                     # Russian Documentation Suite
    └── zh/                     # Simplified Chinese Documentation Suite
```

---

## 🎯 Master Topic Navigation

- **[System Architecture & SOLID](architecture.md)**
- **[Synapse HFT Protocol API Reference](api_reference.md)**
- **[Topology Analysis & SUMO Parsers](topology_analysis.md)**
- **[Traffic Simulation Mechanics](traffic_simulation.md)**
- **[Tkinter UI & Test Harness](ui_and_test_harness.md)**
- **[Testing & Automated Verification](testing.md)**
- **[Developer & Integration Guides](developer_guides.md)**
- **[Deployment & Execution Automation](deployment_and_packaging.md)**

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Canonical Master MOC</i><br/>
  <small>Licensed under <a href="../../LICENSE">Apache 2.0</a> (SPDX-License-Identifier: <code>Apache-2.0</code>). © 2026 Gabriel Moraes - Noxfort Systems.</small>
</div>

