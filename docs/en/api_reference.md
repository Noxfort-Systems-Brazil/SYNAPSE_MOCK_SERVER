---
tags: [api, grpc, reference, protobuf, hft]
aliases: [API Reference, Synapse HFT, gRPC Interface]
---

# ⚡ API Reference & Synapse HFT Protocol Specifications

This document provides the authoritative API specification for the **Synapse HFT** gRPC protocol utilized by SYNAPSE MOCK SERVER.

⬅️ Back to [Main Documentation Hub](synapse_mock_moc.md) | 🏛️ See [Architecture](architecture.md) | 🚗 See [Traffic Simulation](traffic_simulation.md)

---

## 1. gRPC Service Contract: `HFTLink` (`proto/synapse_hft.proto`)

SYNAPSE MOCK SERVER acts as a high-frequency client to the `HFTLink` gRPC service implemented by CARINA or any compatible HFT telemetry receiver.

- **Default Port:** `50051`
- **Transport:** HTTP/2 over TCP
- **Package:** `synapse.hft`

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

## 2. RPC Methods Breakdown

### 2.1 `Ping`
- **Signature:** `rpc Ping (Empty) returns (SystemState)`
- **Request:** Empty message (`{}`).
- **Response:** `SystemState` containing server status, active state, and UTC server timestamp.

### 2.2 `LoadScenario`
- **Signature:** `rpc LoadScenario (ScenarioDefinition) returns (ScenarioStatus)`
- **Request:** `ScenarioDefinition` payload containing compressed map binary (`.net.xml.gz`), SHA-256 hash, and ADAGIO `peak_schedule_json`.
- **Response:** `ScenarioStatus` (`accepted` boolean and descriptive message).

### 2.3 `SystemControl`
- **Signature:** `rpc SystemControl (ControlCommand) returns (CommandResponse)`
- **Request:** `ControlCommand` with action enum (`START`, `PAUSE`, `STOP`, `RESET`).
- **Response:** `CommandResponse` (`success` and `new_state`).

### 2.4 `StreamTraffic`
- **Signature:** `rpc StreamTraffic (stream TrafficFrame) returns (SystemState)`
- **Pattern:** Client-Side Streaming.
- **Request:** Continuous stream of `TrafficFrame` messages.
- **Response:** `SystemState` returned when the client closes the stream.

---

## 3. Message Schemas & Telemetry Structures

```protobuf
message TrafficFrame {
  double timestamp = 1;
  uint64 sequence_id = 2;
  map<string, EdgeState> edges = 3;
}

message EdgeState {
  float occupancy = 1;      // Ratio [0.0 - 1.0] of road occupancy
  float mean_speed = 2;     // Space-mean speed in km/h
  int32 queue_length = 3;   // Number of queued vehicles
  float density = 4;        // Vehicles per kilometer
}
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Protocol API Reference • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
