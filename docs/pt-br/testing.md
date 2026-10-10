---
tags: [testing, qa, validation, unit_tests, verification]
aliases: [Testes e Qualidade, Validação, Suíte de Testes]
---

# 🧪 Testes Automatizados & Qualidade de Software

Este documento apresenta a estrutura de testes automatizados e orientações para criação de mocks no **SYNAPSE MOCK SERVER**.

⬅️ Voltar para o [Hub de Documentação](synapse_mock_moc.md) | 🏛️ Ver [Arquitetura](architecture.md) | 🗺️ Ver [Topologia](topology_analysis.md)

---

## 1. Execução dos Testes

### 1.1 Testes Unitários de Topologia
Valida a extração de redes SUMO e os algoritmos de consulta de arestas adjacentes:

```bash
python test_topology_analyzer.py
```

### 1.2 Teste Rápido de Integração
Executa a validação do pipeline de dados e das interfaces:

```bash
python simple_test.py
```

---

## 2. Mocking com Interfaces SOLID

A injeção de dependências no construtor de `TopologyAnalyzer` permite escrever testes unitários ágeis e sem dependência de arquivos reais no disco:

```python
from interfaces.parser_interface import FileParser
from infrastructure.topology_analyzer import TopologyAnalyzer

class MockParser(FileParser):
    def parse_file(self, file_path):
        return {"simulado": True}

analyzer = TopologyAnalyzer(parser=MockParser())
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Testes Automatizados</i>
</div>
