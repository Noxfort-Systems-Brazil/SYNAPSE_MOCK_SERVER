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

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Deploy e Automação</i>
</div>
