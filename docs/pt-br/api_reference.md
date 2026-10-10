---
tags: [api, grpc, reference, protobuf, hft]
aliases: [Referência da API, Synapse HFT, Interface gRPC]
---

# ⚡ Referência da API & Protocolo Synapse HFT

Este documento detalha o contrato de interface gRPC e as mensagens Protobuf que compõem o protocolo **Synapse HFT**, implementado pelo cliente no **SYNAPSE MOCK SERVER**.

⬅️ Voltar para o [Hub de Documentação](synapse_mock_moc.md) | 🏛️ Ver [Arquitetura](architecture.md) | 🚗 Ver [Simulação de Tráfego](traffic_simulation.md)

---

## 1. Definição do Serviço: `HFTLink` (`proto/synapse_hft.proto`)

O `SYNAPSE MOCK SERVER` conecta-se como cliente ao serviço gRPC `HFTLink` exposto pelo controlador central (porta padrão `50051`):

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

## 2. Métodos e RPCs

### 2.1 `Ping`
- **Requisição:** Mensagem vazia `Empty`.
- **Resposta:** `SystemState` com estado operacional (`active`, `state`, `server_time`).

### 2.2 `LoadScenario`
- **Requisição:** `ScenarioDefinition` contendo o conteúdo binário compactado da rede viária (`.net.xml.gz`), o hash SHA-256 do arquivo, o nome do arquivo e a grade horária `peak_schedule_json` gerada pelo agente classificador ADAGIO.
- **Resposta:** `ScenarioStatus` (`accepted` indicando sucesso e `message`).

### 2.3 `SystemControl`
- **Requisição:** `ControlCommand` com a ação desejada (`START`, `PAUSE`, `STOP`, `RESET`).
- **Resposta:** `CommandResponse` com confirmação `success` e novo estado do servidor.

### 2.4 `StreamTraffic`
- **Comunicação:** Client-side streaming (fluxo contínuo enviado pelo cliente).
- **Requisição:** Fluxo de quadros `TrafficFrame`.
- **Resposta:** `SystemState` final quando o fluxo é encerrado.

---

## 3. Mensagens de Telemetria

```protobuf
message TrafficFrame {
  double timestamp = 1;
  uint64 sequence_id = 2;
  map<string, EdgeState> edges = 3;
}

message EdgeState {
  float occupancy = 1;      // Taxa de ocupação da via [0.0 - 1.0]
  float mean_speed = 2;     // Velocidade média espacial (km/h)
  int32 queue_length = 3;   // Veículos parados em fila
  float density = 4;        // Densidade veicular (veíc/km)
}
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Referência da API</i>
</div>
