# Contributing to SYNAPSE MOCK SERVER

Thank you for your interest in contributing to **SYNAPSE MOCK SERVER**! As part of the CARINA and Noxfort Systems ecosystem, this project provides high-frequency telemetry simulation and testing capabilities for smart city traffic systems.

## Development Setup

1. Clone the repository and create your feature branch:
   ```bash
   git checkout -b feature/my-new-feature
   ```
2. Set up a virtual environment and install runtime requirements:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Read the technical documentation in `docs/` and review the architectural blueprint in `ARCHITECTURE.md`.

## Architectural Guidelines (SOLID Principles)

All new code must adhere to the **SOLID** architectural standards implemented in the project:
1. **Single Responsibility (SRP):** Keep parsers, extractors, queriers, generators, and UI widgets focused on one responsibility.
2. **Open/Closed (OCP):** Extend functionality (such as new map formats or traffic generators) by implementing existing interfaces (`FileParser`, `IDataGenerator`) rather than modifying established core logic.
3. **Liskov Substitution (LSP):** Ensure any new implementation of an interface can be substituted into the system without breaking contracts.
4. **Interface Segregation (ISP):** Avoid fat interfaces; keep contracts small and focused.
5. **Dependency Inversion (DIP):** Depend on abstractions (`interfaces/`), injecting implementations through constructors.

## Testing Guidelines

Before submitting any Pull Request:
1. Run all existing tests to ensure no regressions:
   ```bash
   python test_topology_analyzer.py
   python simple_test.py
   ```
2. If introducing new functionality (e.g. a new generator or parser), provide comprehensive unit tests.

## Pull Request Process

1. Ensure code adheres to PEP 8 standards and is properly documented.
2. Update the documentation in `docs/` or `README.md` if your change alters public interfaces, configuration files, or command-line behavior.
3. Open a Pull Request with a clear title and description of the changes made.
