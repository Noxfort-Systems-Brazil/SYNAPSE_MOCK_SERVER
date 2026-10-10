---
tags: [moc, hub, docs, obsidian, synapse, mock_server, index]
aliases: [MOC Synapse Mock, Hub de Documentação, Conhecimento]
---

<div align="center">

<img src="../assets/synapse-logo.png" alt="SYNAPSE MOCK SERVER Logo" width="120" />

# Hub Técnico de Documentação Mestre (MOC) — SYNAPSE MOCK SERVER
### Índice Central e Knowledge Vault do Ecossistema
*Noxfort Systems — A State Of Art Company*

</div>

Bem-vindo ao centro de documentação técnica oficial do **SYNAPSE MOCK SERVER**. Este documento organiza todos os arquivos, subsistemas e referências técnicas do projeto em conformidade com o GitHub e com o **[Obsidian](https://obsidian.md/)**.

---

## 🗺️ Mapa de Diretórios e Estrutura do Código

```text
Synapse_Mock_Server/
├── main.py                     # Ponto de entrada da aplicação desktop
├── ARCHITECTURE.md             # Blueprint de arquitetura e modelo de threads
├── CHANGELOG.md                # Registro de alterações e histórico de versões
├── CONTRIBUTING.md             # Guia de contribuição e padrões SOLID
├── CODE_OF_CONDUCT.md         # Código de conduta da comunidade
├── SECURITY.md                 # Política de reporte de vulnerabilidades
├── LICENSE                     # Licença Apache 2.0
├── requirements.txt            # Dependências em Python (grpcio, protobuf)
├── run.sh                      # Script de execução com ativação de ambiente
├── peak_schedule.json          # Tabela de horários de pico do agente ADAGIO
├── SOLID_IMPROVEMENTS.md       # Histórico da refatoração SOLID do analisador
├── simple_test.py              # Teste de integração rápido
├── test_topology_analyzer.py   # Testes unitários do grafo e consultas
│
├── interfaces/                 # Contratos abstratos (SOLID)
│   ├── parser_interface.py     # Interface FileParser
│   └── topology_interface.py   # Interfaces TopologyExtractor, Querier e Reporter
├── interfaces.py               # Interfaces ISynapseClient e IDataGenerator
│
├── infrastructure/             # Implementações concretas de infraestrutura
│   ├── grpc_client.py          # Cliente gRPC para o serviço HFTLink
│   ├── generator.py            # Gerador de tráfego Random Walk
│   ├── realistic_generator.py  # Gerador realista (curva diurna e 4 estados)
│   ├── parser.py               # Leitor rápido de arestas (.xml e .gz)
│   ├── topology_analyzer.py    # Fachada com injeção de dependências
│   ├── parsers/                # Implementações de parsers
│   │   └── xml_parser.py       # Leitor concreto de arquivos XML e GZ
│   └── topology/               # Módulos de topologia viária
│       ├── topology_extractor.py # Extração de dados (EdgeInfo, JunctionInfo, etc.)
│       ├── topology_querier.py   # Consultas a montante e a jusante
│       └── topology_reporter.py  # Relatório formatado no terminal
│
├── proto/                      # Contratos Protobuf e gRPC
│   ├── synapse_hft.proto       # Definição do serviço HFTLink e mensagens
│   ├── synapse_hft_pb2.py      # Classes geradas pelo protoc
│   └── synapse_hft_pb2_grpc.py # Stubs gRPC gerados pelo protoc
│
├── ui/                         # Camada de apresentação gráfica
│   └── app_ui.py               # Aplicação desktop Tkinter (MockApp)
│
└── docs/                       # Biblioteca de documentação técnica
    ├── README.md               # Hub central de documentação em inglês
    ├── index.md                # Entrada para MkDocs
    ├── SYNAPSE_MOCK_MOC.md     # MOC canônico em inglês
    ├── pt-br/                  # Documentação em Português do Brasil
    │   ├── README.md           # Hub em português
    │   ├── synapse_mock_moc.md # Este documento
    │   ├── architecture.md     # Arquitetura e concorrência
    │   ├── api_reference.md    # Especificação gRPC da API
    │   ├── topology_analysis.md# Análise topológica viária
    │   ├── traffic_simulation.md# Modelagem de tráfego realista
    │   ├── ui_and_test_harness.md# Interface gráfica e logs
    │   ├── testing.md          # Testes e validação
    │   ├── developer_guides.md # Guias para desenvolvedores
    │   └── deployment_and_packaging.md # Deploy e scripts
    ├── en/                     # Documentação canônica em inglês
    ├── es/                     # Documentação em espanhol
    ├── fr/                     # Documentação em francês
    ├── ru/                     # Documentação em russo
    └── zh/                     # Documentação em chinês simplificado
```

---

## 🎯 Navegação Direta por Tema

- **[Arquitetura do Sistema & SOLID](architecture.md)**
- **[Referência da API do Protocolo Synapse HFT](api_reference.md)**
- **[Análise de Topologia & Parsers SUMO](topology_analysis.md)**
- **[Simulação de Tráfego & Modelos Diurnos](traffic_simulation.md)**
- **[Interface Tkinter & Console Desktop](ui_and_test_harness.md)**
- **[Testes Automatizados & Mocks](testing.md)**
- **[Guias do Desenvolvedor](developer_guides.md)**
- **[Execução, Deploy & Script run.sh](deployment_and_packaging.md)**

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Hub MOC</i>
</div>
