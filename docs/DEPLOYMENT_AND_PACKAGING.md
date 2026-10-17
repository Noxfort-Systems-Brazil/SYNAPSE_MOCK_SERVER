---
tags: [deployment, packaging, runner, shell, environment]
aliases: [Deployment and Packaging, Runner Script, Automation]
---

# 🚀 Deployment, Packaging & Execution Automation

This document outlines deployment procedures, execution automation, system requirements, and launcher scripts for **SYNAPSE MOCK SERVER**.

⬅️ Back to [Main Documentation Hub](SYNAPSE_MOCK_MOC.md) | 🏛️ See [Architecture](ARCHITECTURE.md) | 🛠️ See [Developer Guides](DEVELOPER_GUIDES.md)

---

## 1. System Requirements

- **Operating System:** Linux (Ubuntu 20.04+, Debian 11+, Fedora, Arch), macOS 12+, or Windows 10/11.
- **Python Runtime:** Python 3.10 or newer (Python 3.12 recommended).
- **GUI Subsystem:** Tkinter runtime libraries installed on the host system:
  - Ubuntu/Debian: `sudo apt-get install python3-tk`
  - RedHat/CentOS: `sudo dnf install python3-tkinter`
- **Network Access:** TCP connectivity to the target gRPC server (default port `50051`).

---

## 2. Shell Automation Script: `run.sh`

SYNAPSE MOCK SERVER includes a POSIX shell launcher (`run.sh`) that automates environment activation and passes arbitrary CLI flags directly to `main.py`:

```bash
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Erro: Ambiente virtual não encontrado em .venv ou venv."
    exit 1
fi

python main.py "$@"
```

### 2.1 Usage
```bash
chmod +x run.sh
./run.sh
```

---

## 3. Containerized Execution (Docker)

To run the client inside isolated Docker environments, create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install Tkinter and system libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    tk \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
```

When running GUI applications in Docker on Linux, attach the host X11 socket:
```bash
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --network host \
    synapse-mock-server
```

## 4. Modern Python Packaging: `pyproject.toml` (PEP 621 & PEP 639)

SYNAPSE MOCK SERVER provides modern packaging metadata configured in `pyproject.toml`, fully compliant with **PEP 621** (Project Metadata) and **PEP 639** (SPDX License Expressions).

### 4.1 Direct SPDX License Identifier Declaration
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

### 4.2 Local Installation & CLI Entry Points
The package exposes a standard CLI entry point (`synapse-mock`) mapping directly to `main:main`. You can install the package in editable or production mode:

```bash
# Editable development install
pip install -e .

# Run via installed CLI entry point
synapse-mock
```

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Deployment & Packaging Guide • SYNAPSE MOCK SERVER v1.2.0</i><br/>
  <small>Licensed under <a href="../LICENSE">Apache 2.0</a> (SPDX-License-Identifier: <code>Apache-2.0</code>). © 2026 Gabriel Moraes - Noxfort Systems.</small>
</div>

