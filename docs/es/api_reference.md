---
tags: [api, grpc, reference, protobuf, hft]
aliases: [Referencia API, Synapse HFT, Protocolo gRPC]
---

# ⚡ Referencia de la API & Protocolo Synapse HFT

Este documento detalla el contrato de servicio gRPC y los mensajes Protobuf del protocolo **Synapse HFT** utilizados en SYNAPSE MOCK SERVER.

⬅️ Volver al [Centro de Documentación](README.md) | 🏛️ Ver [Arquitectura](architecture.md) | 🚗 Ver [Simulación](traffic_simulation.md)

---

## 1. Servicio gRPC `HFTLink` (`proto/synapse_hft.proto`)

```protobuf
syntax = "proto3";

package synapse.hft;

service HFTLink {
  rpc Ping (Empty) returns (SystemState);
  rpc LoadScenario (ScenarioDefinition) returns (ScenarioStatus);
  rpc SystemControl (ControlCommand) returns (CommandResponse);
  rpc StreamTraffic (stream TrafficFrame) returns (SystemState);
}
```

---

## 2. Métodos Principales

- **`Ping`**: Verifica disponibilidad del servidor y marca de tiempo UTC.
- **`LoadScenario`**: Transmite mapa comprimido `.net.xml.gz`, hash SHA-256 y programación `peak_schedule.json`.
- **`SystemControl`**: Envía comando de control (`START`, `PAUSE`, `STOP`, `RESET`).
- **`StreamTraffic`**: Flujo continuo de tramas `TrafficFrame` hacia el servidor.

---

## 3. Mensajes de Telemetría

```protobuf
message TrafficFrame {
  double timestamp = 1;
  uint64 sequence_id = 2;
  map<string, EdgeState> edges = 3;
}

message EdgeState {
  float occupancy = 1;      // Ocupación de la vía [0.0 - 1.0]
  float mean_speed = 2;     // Velocidad media espacial (km/h)
  int32 queue_length = 3;   // Longitud de cola en vehículos
  float density = 4;        // Densidad (veh/km)
}
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Referencia API</i>
</div>
