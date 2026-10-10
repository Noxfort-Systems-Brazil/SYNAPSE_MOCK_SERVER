---
tags: [simulation, traffic, generators, dynamics, realistic]
aliases: [Traffic Simulation, Telemetry Generators, Diurnal Model]
---

# 🚗 Traffic Simulation Engine & Telemetry Generators

This document details the mathematical models, temporal dynamics, and stochastic formulations powering the **Traffic Simulation Engine** in SYNAPSE MOCK SERVER.

⬅️ Back to [Main Documentation Hub](synapse_mock_moc.md) | 🏛️ See [Architecture](architecture.md) | ⚡ See [API Reference](api_reference.md)

---

## 1. Generator Interface Contract (`interfaces.py`)

All telemetry generators implement the `IDataGenerator` abstraction:

```python
class IDataGenerator(ABC):
    @abstractmethod
    def generate_frame(self, sequence_id: int) -> dict:
        """Generates a single TrafficFrame payload."""
        pass
```

---

## 2. Realistic Diurnal Generator (`RealisticTrafficGenerator`)

The `RealisticTrafficGenerator` provides high-fidelity simulation by coupling macroscopic 24-hour diurnal flow curves with microscopic 1-minute congestion regimes.

### 2.1 Diurnal Time-of-Day Modulation ($F(h)$)

Traffic intensity scales with local wall-clock hours $h \in [0, 23]$:
- **02:00 – 05:00:** Night minimum (factor $0.2$).
- **06:00 – 08:00:** Morning ramp-up.
- **09:00 – 11:00:** Morning rush (factor up to $0.8$).
- **12:00 – 15:00:** Midday moderate wave.
- **16:00 – 19:00:** Evening peak rush (factor up to $0.9$).
- **20:00 – 01:00:** Night decay.

### 2.2 Deterministic 1-Minute State Seeding

In physical traffic networks, shockwaves and congestion clusters persist over multiple minutes rather than fluctuating erratically every 50 ms. To reproduce this physical inertia:

$$\text{MinuteBlock} = \left\lfloor \frac{t_{\text{current}}}{60} \right\rfloor$$
$$\text{Seed} = \text{MinuteBlock} \mathbin{\Vert} \text{edge\_id}$$

The random number generator is seeded with this composite token, guaranteeing that each edge remains locked into a specific congestion scenario for exactly 60 seconds before transitioning smoothly.

### 2.3 The 4 Critical Traffic Congestion Regimes

| Scenario Index | Regime | Occupancy Range | Mean Speed (km/h) | Vehicle Density (veh/km) | Typical Queue |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **0** | **Via Livre (Free Flow)** | $0.00 - 0.20$ | $70.0 - 120.0$ | $0.0 - 20.0$ | $0 - 5$ |
| **1** | **Tráfego Moderado (Moderate)** | $0.30 - 0.50$ | $40.0 - 60.0$ | $30.0 - 50.0$ | $10 - 20$ |
| **2** | **Congestionamento Leve (Light)** | $0.60 - 0.80$ | $20.0 - 35.0$ | $60.0 - 90.0$ | $30 - 60$ |
| **3** | **Congestionamento Severo (Severe)** | $0.85 - 1.00$ | $2.0 - 8.0$ | $100.0 - 150.0$ | $80 - 150$ |

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Traffic Simulation Guide • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
