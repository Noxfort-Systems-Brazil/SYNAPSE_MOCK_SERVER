---
tags: [readme, home, synapse, mock_server, test_harness]
aliases: [Synapse Mock Server, Root]
---

<div align="center">

<img src="docs/assets/carina-logo.png" alt="SYNAPSE MOCK SERVER Logo" width="130" />

# SYNAPSE MOCK SERVER
### High-Frequency Telemetry (HFT) Client Test Harness & Traffic Simulator
*Noxfort Systems — A State Of Art Company*

[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/Synapse_Mock_Server)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Protocol Buffers](https://img.shields.io/badge/Protobuf-v4.25%2B-blue?style=flat)](https://protobuf.dev/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat)](LICENSE)

---

🌐 **Translations / Idiomas:** **[🇺🇸 English](docs/en/README.md)** • **[🇧🇷 Português do Brasil](docs/pt-br/README.md)** • **[🇪🇸 Español](docs/es/README.md)** • **[🇫🇷 Français](docs/fr/README.md)** • **[🇷🇺 Русский](docs/ru/README.md)** • **[🇨🇳 简体中文](docs/zh/README.md)** • **[📚 Documentation Hub](docs/README.md)**

---

</div>

**SYNAPSE MOCK SERVER** is an open-source High-Frequency Telemetry (HFT) client test harness and traffic load simulator for the Synapse protocol within the CARINA intelligent mobility ecosystem. Built in Python under strict **Clean Architecture** and **SOLID** principles, it serves as the official client simulation engine to benchmark, load-test, and validate real-time intelligent traffic control agents, digital twin infrastructures, and gRPC servers.

---

## 📚 Documentation Hub & Knowledge Vault

Explore the full architecture, internal mechanics, protocol specifications, and developer guides:

| Card / Subsystem | Focus Area | Direct Link |
| :--- | :--- | :---: |
| 📚 **Documentation Hub** | Central Multi-Language Index & Direct Topic Matrix | [Explore Hub](docs/README.md) |
| 🗺️ **Master MOC** | Master Map of Content & Obsidian Knowledge Vault index | [View MOC](docs/SYNAPSE_MOCK_MOC.md) |
| 🏛️ **Core Architecture** | SOLID Clean Architecture, Dependency Injection & Concurrency | [View Blueprint](ARCHITECTURE.md) |
| ⚡ **Synapse HFT API** | gRPC `HFTLink` interface (`Ping`, `LoadScenario`, `Control`, `Stream`) | [View API Reference](docs/API_REFERENCE.md) |
| 🗺️ **Topology Analysis Engine** | SUMO `.net.xml.gz` Parsing, Graph Extractors & Adjacency Queries | [View Topology Guide](docs/TOPOLOGY_ANALYSIS.md) |
| 🚗 **Traffic Simulation Engine** | Diurnal Time-of-Day Curves & 4 Congestion States | [View Simulation Guide](docs/TRAFFIC_SIMULATION.md) |
| 🖥️ **Tkinter UI & Test Harness** | Desktop Dark Dashboard, Thread-Safe Logging & Status Feedback | [View UI Guide](docs/UI_AND_TEST_HARNESS.md) |
| 🧪 **Testing & Verification** | Topology verification, test scripts and quality assurance | [View Guidelines](docs/TESTING.md) |
| 🛠️ **Developer Guides** | Protobuf compilation, custom traffic generators & SOLID extensions | [View Guides](docs/DEVELOPER_GUIDES.md) |
| 🚀 **Deployment & Packaging** | Virtual environment automation, launcher scripts & containerization | [View Deployment](docs/DEPLOYMENT_AND_PACKAGING.md) |

---

## ⚡ Key Architectural Capabilities

- **Synapse HFT Client Engine (Sub-Millisecond gRPC):** High-throughput gRPC client implementing the `HFTLink` service contract (`Ping`, `LoadScenario`, `SystemControl`, `StreamTraffic`) with resilient auto-reconnect and client-side streaming at 10–20 Hz (50–100 ms interval).
- **Diurnal Realistic Traffic Generator (`RealisticTrafficGenerator`):** Models real-world macroscopic traffic dynamics based on local time-of-day curves (morning peak 7–9h, evening peak 16–19h, midday 12–15h, night minimum 2–5h) coupled with 4 deterministic 1-minute scenario states (*Via Livre*, *Tráfego Moderado*, *Congestionamento Leve*, *Congestionamento Severo*) with continuous stochastic jitter.
- **Random Walk Fallback Generator (`RandomTrafficGenerator`):** Bounded random-walk generator for unit tests and synthetic edge stress testing.
- **SOLID SUMO Topology Analyzer (`TopologyAnalyzer`):** Refactored modular pipeline isolating file parsing (`FileParser` / `XMLParser`), topology extraction (`TopologyExtractor`), relationship querying (`TopologyQuerier`), and formatted reporting (`TopologyReporter`).
- **Interactive Desktop UI Test Harness (`MockApp`):** Lightweight, dark-themed Tkinter console with file dialog validation for `.net.xml.gz` networks, decoupled background simulation worker (`threading.Thread`), and thread-safe console logging via `root.after`.
- **Zero-Touch Execution (`run.sh`):** Shell launcher automatically locating and activating project virtual environments (`.venv` or `venv`) before executing the test harness.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+ (Python 3.12 recommended)
- Tkinter (standard on Windows/macOS; on Ubuntu/Debian: `sudo apt-get install python3-tk`)
- gRPC & Protobuf runtimes

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Noxfort-Systems-Brazil/Synapse_Mock_Server.git
cd Synapse_Mock_Server

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Running with Launcher Script
```bash
chmod +x run.sh
./run.sh
```

### 4. Running Directly via Python
```bash
python main.py
```

---

## 🧪 Running Automated Tests

```bash
# Run topology analyzer tests
python test_topology_analyzer.py

# Run simple integration test
python simple_test.py
```

---

<div align="center">
  <img src="docs/assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="48" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>High-Frequency Telemetry (HFT) Client Test Harness • SYNAPSE MOCK SERVER v1.2.0</i><br/>
  <small>Licensed under the <a href="LICENSE">Apache License 2.0</a>. © 2026 Gabriel Moraes - Noxfort Systems.</small>
</div>
