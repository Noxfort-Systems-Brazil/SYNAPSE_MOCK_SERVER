---
tags: [simulation, traffic, generators, dynamics, realistic]
aliases: [Simulación de Tráfico, Modelos de Telemetría]
---

# 🚗 Simulación de Tráfico & Modelos de Telemetría

Este documento detalla la formulación matemática del generador de tráfico diurno y los 4 regímenes de congestión del **SYNAPSE MOCK SERVER**.

⬅️ Volver al [Centro de Documentación](README.md) | 🏛️ Ver [Arquitectura](architecture.md) | ⚡ Ver [API](api_reference.md)

---

## 1. Generador Realista Diurno (`RealisticTrafficGenerator`)

El generador modula el flujo según el ciclo diario:
- **02:00 a 05:00:** Mínimo nocturno (factor $0.2$).
- **06:00 a 08:00:** Rampa matutina ascendente.
- **09:00 a 11:00:** Hora pico de la mañana.
- **12:00 a 15:00:** Flujo moderado diurno.
- **16:00 a 19:00:** Hora pico de la tarde.
- **20:00 a 01:00:** Descenso nocturno.

### 1.1 Anclaje Determinista de 1 Minuto
Para emular la inercia del tráfico físico, cada tramo fija su estado aleatorio según el bloque de 60 segundos actual y el ID del tramo:

$$\text{Seed} = \left\lfloor \frac{t}{60} \right\rfloor \mathbin{\Vert} \text{edge\_id}$$

### 1.2 Los 4 Regímenes de Tráfico
1. **Vía Libre:** Ocupación $0.00 - 0.20$, velocidad $70 - 120\text{ km/h}$.
2. **Tráfico Moderado:** Ocupación $0.30 - 0.50$, velocidad $40 - 60\text{ km/h}$.
3. **Congestión Leve:** Ocupación $0.60 - 0.80$, velocidad $20 - 35\text{ km/h}$.
4. **Congestión Severa:** Ocupación $0.85 - 1.00$, velocidad $2 - 8\text{ km/h}$.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Simulación de Tráfico</i>
</div>
