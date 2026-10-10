---
tags: [simulation, traffic, generators, dynamics, realistic]
aliases: [Simulação de Tráfego, Geradores de Telemetria, Modelo Diurno]
---

# 🚗 Simulação de Tráfego & Geradores de Telemetria

Este documento apresenta os princípios matemáticos e modelos de geração de telemetria empregados no **SYNAPSE MOCK SERVER**.

⬅️ Voltar para o [Hub de Documentação](synapse_mock_moc.md) | 🏛️ Ver [Arquitetura](architecture.md) | ⚡ Ver [API](api_reference.md)

---

## 1. Contrato `IDataGenerator`

Todos os geradores de telemetria implementam a interface `IDataGenerator` definida em `interfaces.py`:

```python
class IDataGenerator(ABC):
    @abstractmethod
    def generate_frame(self, sequence_id: int) -> dict:
        """Gera um dicionário correspondente ao quadro de telemetria."""
        pass
```

---

## 2. Gerador Realista (`RealisticTrafficGenerator`)

O `RealisticTrafficGenerator` combina modelagem de tráfego em escala macroscópica (curva diurna horária) com transições microscópicas estáveis no tempo.

### 2.1 Curva de Tráfego Diurna
O fluxo varia segundo o horário local do sistema:
- **02:00 às 05:00:** Mínimo noturno (fator $0.2$).
- **06:00 às 08:00:** Rampa matutina crescente.
- **09:00 às 11:00:** Pico matutino (fator até $0.8$).
- **12:00 às 15:00:** Período de entre-picos com fluxo moderado.
- **16:00 às 19:00:** Pico vespertino intenso (fator até $0.9$).
- **20:00 às 01:00:** Desaceleração noturna progressiva.

### 2.2 Semente Determinística por Bloco de 1 Minuto
Em redes reais, congestionamentos não surgem nem desaparecem a cada 50 milissegundos. Para emular essa inércia física, o gerador ancora a semente aleatória no minuto atual e no identificador da via:

$$\text{Seed} = \left\lfloor \frac{t}{60} \right\rfloor \mathbin{\Vert} \text{edge\_id}$$

Isso garante que cada via permaneça no mesmo regime de tráfego por 1 minuto completo antes de migrar de estado, recebendo apenas pequenas oscilações de ruído (jitter) entre quadros.

### 2.3 Os 4 Estados Críticos de Tráfego

| Estado | Regime | Ocupação | Velocidade Média | Densidade | Fila Típica |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **0** | **Via Livre** | $0.00 - 0.20$ | $70 - 120\text{ km/h}$ | $0 - 20\text{ v/km}$ | $0 - 5$ |
| **1** | **Tráfego Moderado** | $0.30 - 0.50$ | $40 - 60\text{ km/h}$ | $30 - 50\text{ v/km}$ | $10 - 20$ |
| **2** | **Congestionamento Leve** | $0.60 - 0.80$ | $20 - 35\text{ km/h}$ | $60 - 90\text{ v/km}$ | $30 - 60$ |
| **3** | **Congestionamento Severo** | $0.85 - 1.00$ | $2 - 8\text{ km/h}$ | $100 - 150\text{ v/km}$ | $80 - 150$ |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Simulação de Tráfego</i>
</div>
