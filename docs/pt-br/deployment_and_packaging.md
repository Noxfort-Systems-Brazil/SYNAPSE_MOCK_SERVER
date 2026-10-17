---
tags: [deployment, packaging, runner, shell, environment]
aliases: [Deploy e Empacotamento, Automação, Script Runner]
---

# 🚀 Deploy, Empacotamento & Automação de Execução

Este documento aborda a execução automatizada, requisitos de sistema e empacotamento do **SYNAPSE MOCK SERVER**.

⬅️ Voltar para o [Hub de Documentação](synapse_mock_moc.md) | 🏛️ Ver [Arquitetura](architecture.md) | 🛠️ Ver [Guias](developer_guides.md)

---

## 1. Requisitos de Sistema

- **Sistema Operacional:** Linux (Ubuntu 20.04+, Debian 11+), macOS 12+ ou Windows 10/11.
- **Python:** Versão 3.10 ou superior (3.12 recomendada).
- **Bibliotecas Gráficas:** Suporte a Tkinter instalado no sistema operacional:
  - No Ubuntu/Debian: `sudo apt-get install python3-tk`
- **Rede:** Conexão TCP à porta `50051` da máquina onde o servidor CARINA está executando.

---

## 2. Automação com `run.sh`

O projeto inclui o script de shell POSIX `run.sh` que localiza e ativa o ambiente virtual automaticamente:

```bash
chmod +x run.sh
./run.sh
```

---

## 3. Empacotamento Python & `pyproject.toml` (PEP 621 & PEP 639)

O SYNAPSE MOCK SERVER fornece metadados modernos de empacotamento configurados em `pyproject.toml`, em total conformidade com a **PEP 621** (Metadados de Projeto) e a **PEP 639** (Expressões de Licença SPDX).

### 3.1 Declaração Direta do Identificador SPDX
Sob a PEP 639, a expressão da licença é declarada diretamente sob a seção `[project]` como uma string identificadora SPDX padronizada, eliminando campos de texto livre legados e classifiers depreciados:

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

### 3.2 Instalação Local & Entry Points de CLI
O pacote disponibiliza um comando CLI nativo (`synapse-mock`) mapeado para o entry point `main:main`:

```bash
# Instalação em modo editável para desenvolvimento
pip install -e .

# Execução direta pelo comando CLI registrado
synapse-mock
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Deploy e Automação</i><br/>
  <small>Licenciado sob <a href="../../LICENSE">Apache 2.0</a> (SPDX-License-Identifier: <code>Apache-2.0</code>). © 2026 Gabriel Moraes - Noxfort Systems.</small>
</div>

