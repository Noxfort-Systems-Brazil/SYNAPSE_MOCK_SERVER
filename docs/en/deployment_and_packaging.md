---
tags: [deployment, packaging, runner, shell, environment]
aliases: [Deployment and Packaging, Runner Script, Automation]
---

# 🚀 Deployment, Packaging & Execution Automation

This document outlines deployment procedures, execution automation, system requirements, and launcher scripts for **SYNAPSE MOCK SERVER**.

⬅️ Back to [Main Documentation Hub](synapse_mock_moc.md) | 🏛️ See [Architecture](architecture.md) | 🛠️ See [Developer Guides](developer_guides.md)

---

## 1. System Requirements

- **Operating System:** Linux (Ubuntu 20.04+, Debian 11+), macOS 12+, or Windows 10/11.
- **Python Runtime:** Python 3.10 or newer (Python 3.12 recommended).
- **GUI Subsystem:** Tkinter runtime libraries installed on the host system:
  - Ubuntu/Debian: `sudo apt-get install python3-tk`
- **Network Access:** TCP connectivity to the target gRPC server (port `50051`).

---

## 2. Shell Automation Script: `run.sh`

```bash
chmod +x run.sh
./run.sh
```

---

## 3. Python Packaging & `pyproject.toml` (PEP 621 & PEP 639)

SYNAPSE MOCK SERVER provides modern packaging metadata configured in `pyproject.toml`, fully compliant with **PEP 621** (Project Metadata) and **PEP 639** (SPDX License Expressions).

### 3.1 Direct SPDX License Identifier Declaration
Under PEP 639, the license expression is declared directly within the `[project]` table as a standardized SPDX identifier string, eliminating legacy free-text fields and deprecated classifiers:

```toml
[project]
name = "synapse-mock-server"
version = "1.2.0"
description = "High-Frequency Telemetry (HFT) Client Test Harness & Traffic Simulator for the Synapse protocol"
readme = "README.md"
requires-python = ">=3.10"
license = "Apache-2.0"
license-files = ["LICENSE"]
```

### 3.2 CLI Entry Points & Installation
The package provides a built-in CLI command (`synapse-mock`) mapped to `main:main`:

```bash
# Editable install
pip install -e .

# Run via entry point
synapse-mock
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Deployment & Packaging Guide • SYNAPSE MOCK SERVER v1.2.0</i><br/>
  <small>Licensed under <a href="../../LICENSE">Apache 2.0</a> (SPDX-License-Identifier: <code>Apache-2.0</code>). © 2026 Gabriel Moraes - Noxfort Systems.</small>
</div>

