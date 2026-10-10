<div align="center">

# SYNAPSE MOCK SERVER — Hub de Documentação
### Central de Documentação Técnica e Guias do Desenvolvedor
*Noxfort Systems — A State Of Art Company*

[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/Synapse_Mock_Server)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Protocol Buffers](https://img.shields.io/badge/Protobuf-v4.25%2B-blue?style=flat)](https://protobuf.dev/)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-Apache_2.0-blue?style=flat)](../../LICENSE)

---

### 🌐 Seleção de Idiomas

[**🇺🇸 English**](../en/README.md) • [**🇧🇷 Português (Brasil)**](README.md) • [**🇪🇸 Español**](../es/README.md) • [**🇫🇷 Français**](../fr/README.md) • [**🇷🇺 Русский**](../ru/README.md) • [**🇨🇳 简体中文**](../zh/README.md)

---

</div>

Bem-vindo à documentação oficial em Português do Brasil do **SYNAPSE MOCK SERVER**.

O **SYNAPSE MOCK SERVER** é o gerador de carga de telemetria e harness de testes de cliente oficial para o protocolo Synapse HFT no ecossistema CARINA. Ele permite reproduzir dinâmicas reais de tráfego, carregar redes viárias do simulador SUMO e transmitir fluxos contínuos via gRPC a 10–20 Hz para testar a robustez dos controladores inteligentes.

---

## 📚 Navegação por Módulos Técnicos

| Dimensão / Módulo | Descrição | Link Direto |
| :--- | :--- | :---: |
| 🗺️ **MOC Mestre** | Mapa central de conteúdo e estrutura do repositório | [Ver MOC](synapse_mock_moc.md) |
| 🏛️ **Arquitetura do Sistema** | Padrões Clean Architecture, SOLID e concorrência multithread | [Ver Arquitetura](architecture.md) |
| ⚡ **Referência da API gRPC** | Especificação do serviço `HFTLink` e payloads de telemetria | [Ver API](api_reference.md) |
| 🗺️ **Análise de Topologia** | Parsers SUMO, extração de vias e consultas de conectividade | [Ver Topologia](topology_analysis.md) |
| 🚗 **Simulação de Tráfego** | Curvas diurnas, 4 estados de tráfego e gerador randômico | [Ver Simulação](traffic_simulation.md) |
| 🖥️ **Interface Gráfica & Console** | Painel desktop Tkinter, threads em segundo plano e logs | [Ver Interface](ui_and_test_harness.md) |
| 🧪 **Testes & Qualidade** | Testes automatizados do analisador topológico e mocks | [Ver Testes](testing.md) |
| 🛠️ **Guias do Desenvolvedor** | Setup do ambiente, compilação de `.proto` e novos geradores | [Ver Guias](developer_guides.md) |
| 🚀 **Deploy & Automação** | Script de execução `run.sh`, virtualenv e conteinerização | [Ver Deploy](deployment_and_packaging.md) |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Documentação Técnica</i>
</div>
