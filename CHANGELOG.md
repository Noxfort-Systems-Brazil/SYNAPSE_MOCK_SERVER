# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-10-10

### Added
- **SOLID Architecture Refactoring (`interfaces/` & `infrastructure/topology/`)**: Complete decoupling of `TopologyAnalyzer` into cohesive single-responsibility components (`FileParser`, `TopologyExtractor`, `TopologyQuerier`, `TopologyReporter`) with constructor Dependency Injection.
- **Enterprise Documentation Suite (`docs/` & `mkdocs.yml`)**: Full multi-language technical documentation vault (en, pt-br, es, fr, ru, zh), master Obsidian MOC, architectural blueprints, API references, and Material for MkDocs configuration.
- **Automated Launcher Script (`run.sh`)**: Posix-compliant launcher with automatic detection and activation of local virtual environments (`.venv` or `venv`) passing CLI arguments directly to `main.py`.
- **Topological Query Verification (`test_topology_analyzer.py`)**: Dedicated test suite validating upstream and downstream edge relationship querying.

### Changed
- **Enhanced UI Feedback (`ui/app_ui.py`)**: Integrated real-time edge telemetry sampling (occupancy, speed, density) in the dark console logger every 10 frames to avoid GUI spam.
- **Scenario Metadata Support**: Enhanced `LoadScenario` in `GRPCClient` to dynamically ingest and transmit ADAGIO `peak_schedule.json`.

---

## [1.1.0] - 2026-10-05

### Added
- **Realistic Diurnal Traffic Generator (`infrastructure/realistic_generator.py`)**: Models 24-hour diurnal traffic flow curves (morning rush, evening peak, midday, night minimum) with deterministic 1-minute scenario seeding (*Via Livre*, *Tráfego Moderado*, *Congestionamento Leve*, *Congestionamento Severo*) and continuous micro-jitter.
- **Fast SUMO Network Parser (`infrastructure/parser.py`)**: High-speed edge ID extraction from both plain `.net.xml` and gzip-compressed `.net.xml.gz` files, filtering out internal junction links (`:`).

### Changed
- **Resilient Auto-Reconnect Loop**: Enhanced worker thread in `MockApp` to automatically retry connecting and reloading scenarios upon connection drop.

---

## [1.0.0] - 2026-09-20

### Added
- **Initial Release of Synapse Mock Server**: Open-source test harness and telemetry load simulator for the Synapse HFT protocol.
- **gRPC Client Stub (`infrastructure/grpc_client.py`)**: Implements client-side calls for `Ping`, `LoadScenario`, `SystemControl`, and high-frequency `StreamTraffic`.
- **Tkinter Desktop Interface (`ui/app_ui.py`)**: Graphical interface with map selection dialog, Play/Stop controls, and dark terminal output.
- **Protobuf Specifications (`proto/synapse_hft.proto`)**: Core schema for `HFTLink` gRPC services, topology graphs, and edge states.
- **Random Walk Generator (`infrastructure/generator.py`)**: Baseline synthetic generator for stress-testing.
