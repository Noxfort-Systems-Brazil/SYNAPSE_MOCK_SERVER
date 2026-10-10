---
tags: [api, grpc, reference, protobuf, hft]
aliases: [Référence API, Protocole Synapse HFT]
---

# ⚡ Référence API & Protocole Synapse HFT

Ce document détaille la spécification du service gRPC `HFTLink` (`proto/synapse_hft.proto`).

⬅️ Retour au [Hub de Documentation](README.md) | 🏛️ Voir [Architecture](architecture.md)

---

## 1. Service gRPC `HFTLink`

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

- **`Ping`**: Vérifie la connectivité et l'horodatage UTC du serveur.
- **`LoadScenario`**: Transfère le réseau compressé `.net.xml.gz` et son hash SHA-256.
- **`SystemControl`**: Exécute des actions de contrôle (`START`, `STOP`).
- **`StreamTraffic`**: Flux continu de trames de trafic `TrafficFrame`.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Référence API</i>
</div>
