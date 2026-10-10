---
tags: [api, grpc, reference, protobuf, hft]
aliases: [Спецификация API, Протокол Synapse HFT]
---

# ⚡ Спецификация API & Протокол Synapse HFT

Документ описывает контракт gRPC сервиса `HFTLink` (`proto/synapse_hft.proto`).

⬅️ Назад в [Центр документации](README.md) | 🏛️ См. [Архитектуру](architecture.md)

---

## 1. Сервис `HFTLink`

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

- **`Ping`**: Проверка активности и получение времени сервера.
- **`LoadScenario`**: Передача сжатой карты `.net.xml.gz` с хешем SHA-256 и расписанием ADAGIO.
- **`SystemControl`**: Команды управления (`START`, `STOP`).
- **`StreamTraffic`**: Потоковая передача кадров `TrafficFrame`.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Спецификация API</i>
</div>
