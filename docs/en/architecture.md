---
tags: [architecture, core, system, solid, grpc, client, simulation]
aliases: [System Architecture, Client Architecture, Blueprint]
---

# 🏛️ SYNAPSE MOCK SERVER: Architecture & System Blueprint

This document details the software engineering architecture of **SYNAPSE MOCK SERVER**. Designed as an industrial test harness for the Synapse HFT protocol, it enforces high decoupling via Clean Architecture and SOLID design patterns.

⬅️ Back to [Main Documentation Hub](synapse_mock_moc.md) | ⚡ See [API Reference](api_reference.md) | 🗺️ See [Topology Analysis](topology_analysis.md) | 🚗 See [Traffic Simulation](traffic_simulation.md)

---

## 1. System Decomposition & Layering

The application is structured into four distinct logical layers:

```mermaid
graph TD
    subgraph 1. Presentation Layer
        UI[Tkinter Desktop App - MockApp]
        CLI[run.sh / main.py Entrypoint]
    end

    subgraph 2. Abstraction Layer
        ISynapseClient[ISynapseClient]
        IDataGenerator[IDataGenerator]
        IFileParser[FileParser]
        ITopologyExtractor[TopologyExtractor]
        ITopologyQuerier[TopologyQuerier]
        ITopologyReporter[TopologyReporter]
    end

    subgraph 3. Infrastructure Layer
        GRPC[GRPCClient]
        XML[XMLParser]
        Extractor[TopologyExtractorImpl]
        Querier[TopologyQuerierImpl]
        Reporter[TopologyReporterImpl]
        Facade[TopologyAnalyzer Facade]
    end

    subgraph 4. Simulation Domain
        Realistic[RealisticTrafficGenerator]
        RandomGen[RandomTrafficGenerator]
    end

    UI --> ISynapseClient
    UI --> IDataGenerator
    CLI --> UI
    GRPC -.-> ISynapseClient
    Realistic -.-> IDataGenerator
    RandomGen -.-> IDataGenerator
    XML -.-> IFileParser
    Extractor -.-> ITopologyExtractor
    Querier -.-> ITopologyQuerier
    Reporter -.-> ITopologyReporter
    Facade --> IFileParser
    Facade --> ITopologyExtractor
    Facade --> ITopologyQuerier
    Facade --> ITopologyReporter
```

---

## 2. SOLID Architectural Principles

The topology analysis module (`infrastructure/topology_analyzer.py`) was restructured to fulfill all 5 SOLID principles:

### 2.1 Single Responsibility Principle (SRP)
- **`XMLParser`**: Solely responsible for XML and GZ parsing into element trees.
- **`TopologyExtractorImpl`**: Solely responsible for mapping XML nodes into strongly-typed dataclasses (`EdgeInfo`, `JunctionInfo`, `ConnectionInfo`).
- **`TopologyQuerierImpl`**: Solely responsible for upstream and downstream adjacency queries.
- **`TopologyReporterImpl`**: Solely responsible for human-readable terminal summaries.
- **`TopologyAnalyzer`**: Functions purely as a coordinator facade.

### 2.2 Open/Closed Principle (OCP)
The system is open for extension without modifying existing code. To support a new network format (such as OpenDRIVE or GeoJSON), implement the `FileParser` interface and inject it into `TopologyAnalyzer`.

### 2.3 Liskov Substitution Principle (LSP)
All concrete implementations can be substituted wherever their corresponding interface is expected without altering correctness or breaking assumptions.

### 2.4 Interface Segregation Principle (ISP)
Client code only depends on the interfaces it consumes (`FileParser`, `TopologyExtractor`, `TopologyQuerier`, `TopologyReporter`).

### 2.5 Dependency Inversion Principle (DIP)
High-level policies depend upon abstract contracts rather than concrete low-level implementations. Constructor injection provides sensible defaults while allowing complete mockability in unit tests.

---

## 3. Concurrency & Multi-Threading Model

Desktop interfaces must remain responsive while high-frequency network streaming occurs. SYNAPSE MOCK SERVER resolves this through multi-threaded decoupling:

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant MainThread as Main Thread (Tkinter GUI)
    participant WorkerThread as Worker Thread (Daemon)
    participant GRPC as GRPCClient
    participant Server as HFTLink gRPC Server

    User->>MainThread: Select Map & Click "▶ Play"
    MainThread->>WorkerThread: Spawn Thread (_run_simulation)
    WorkerThread->>GRPC: connect("localhost:50051")
    WorkerThread->>GRPC: load_scenario(map_path)
    GRPC->>Server: LoadScenario(ScenarioDefinition)
    Server-->>GRPC: ScenarioStatus(accepted=True)
    WorkerThread->>GRPC: system_control("START")
    GRPC->>Server: SystemControl(action=START)
    Server-->>GRPC: CommandResponse(success=True)

    loop High-Frequency Telemetry Stream (10-20 Hz)
        WorkerThread->>WorkerThread: generate_frame()
        WorkerThread->>GRPC: StreamTraffic(TrafficFrame)
        GRPC->>Server: Stream frame
        WorkerThread->>MainThread: root.after(0, update_log)
        MainThread->>MainThread: Write to Console
    end

    User->MainThread: Click "Stop"
    MainThread->>WorkerThread: stop_streaming()
    WorkerThread->>MainThread: Reset GUI State
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>System Architecture • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
