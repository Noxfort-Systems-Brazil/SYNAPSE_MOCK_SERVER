---
tags: [api, grpc, reference, protobuf, hft]
aliases: [API Reference, Synapse HFT, gRPC Interface]
---

# ⚡ API Reference & Synapse HFT Protocol Specifications

This document provides the authoritative API specification for the **Synapse HFT** gRPC protocol utilized by SYNAPSE MOCK SERVER.

⬅️ Back to [Main Documentation Hub](SYNAPSE_MOCK_MOC.md) | 🏛️ See [Architecture Blueprint](ARCHITECTURE.md) | 🚗 See [Traffic Simulation](TRAFFIC_SIMULATION.md)

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
- **Response:** `SystemState` containing:
  - `active` (`bool`): Operational status of the remote server.
  - `state` (`string`): Current operating state (e.g., `"ONLINE"`, `"INITIALIZED"`).
  - `server_time` (`uint64`): Epoch timestamp in microseconds or milliseconds.

### 2.2 `LoadScenario`
- **Signature:** `rpc LoadScenario (ScenarioDefinition) returns (ScenarioStatus)`
- **Request:** `ScenarioDefinition` payload containing:
  - `map_hash` (`string`): SHA-256 hash of the binary map payload.
  - `graph` (`TopologyGraph`): Optional explicit node/edge graph definition.
  - `geometry` (`MapGeometry`): Optional polyline shapes.
  - `map_file_content` (`bytes`): Raw binary bytes of compressed `.net.xml.gz` file.
  - `map_file_name` (`string`): Filename (e.g., `londrina.net.xml.gz`).
  - `peak_schedule_json` (`string`): Serialized JSON schedule from the ADAGIO classifier.
- **Response:** `ScenarioStatus` containing:
  - `accepted` (`bool`): Whether the scenario was validated and stored.
  - `message` (`string`): Informational or error description.

### 2.3 `SystemControl`
- **Signature:** `rpc SystemControl (ControlCommand) returns (CommandResponse)`
- **Request:** `ControlCommand` containing:
  - `action` (`enum Action`):
    - `UNKNOWN = 0`
    - `START = 1`
    - `PAUSE = 2`
    - `STOP = 3`
    - `RESET = 4`
- **Response:** `CommandResponse` containing:
  - `success` (`bool`): Whether command execution succeeded.
  - `new_state` (`string`): Resulting server state.

### 2.4 `StreamTraffic`
- **Signature:** `rpc StreamTraffic (stream TrafficFrame) returns (SystemState)`
- **Communication Pattern:** Client-Side Streaming.
- **Request:** Continuous stream of `TrafficFrame` messages.
- **Response:** `SystemState` returned when the client closes the stream.

---

## 3. Message Schemas & Telemetry Structures

### 3.1 `TrafficFrame`
High-frequency telemetry snapshot across network edges:

```protobuf
message TrafficFrame {
  double timestamp = 1;
  uint64 sequence_id = 2;
  map<string, EdgeState> edges = 3;
}
```

### 3.2 `EdgeState`
Physical flow parameters per street edge:

```protobuf
message EdgeState {
  float occupancy = 1;      // Ratio [0.0 - 1.0] of road occupancy
  float mean_speed = 2;     // Space-mean speed in km/h or m/s
  int32 queue_length = 3;   // Number of queued vehicles
  float density = 4;        // Vehicles per kilometer (veh/km)
}
```

### 3.3 `TopologyGraph`, `TopologyNode`, and `TopologyEdge`

```protobuf
message TopologyGraph {
  repeated TopologyNode nodes = 1;
  repeated TopologyEdge edges = 2;
}

message TopologyNode {
  string id = 1;
  string type = 2;           // e.g., "traffic_light", "priority"
  double x = 3;
  double y = 4;
  string tl_logic_id = 5;    // Traffic light logic identifier
}

message TopologyEdge {
  string id = 1;
  string source_node = 2;
  string target_node = 3;
  double length = 4;
  int32 lanes = 5;
  double max_speed = 6;
  int32 signal_group_id = 7;
}
```

---

## 4. Client Implementation: `GRPCClient` (`infrastructure/grpc_client.py`)

The `GRPCClient` class implements `ISynapseClient` defined in `interfaces.py`:

```python
class ISynapseClient(ABC):
    @abstractmethod
    def connect(self, address: str): pass

    @abstractmethod
    def system_control(self, action: str) -> bool: pass

    @abstractmethod
    def load_scenario(self, map_file_path: str) -> bool: pass

    @abstractmethod
    def stream_traffic(self, generator: IDataGenerator, on_frame_sent=None): pass

    @abstractmethod
    def stop_streaming(self): pass
```

### 4.1 Frame Generator Iterator
During streaming, `GRPCClient.stream_traffic` generates frames using a Python generator:
- Increments `sequence_id` monotonically.
- Converts raw generator dictionaries into Protobuf `TrafficFrame` instances.
- Yields frames into the gRPC stub.
- Introduces random sleep intervals ($t_{\text{sleep}} \in [0.050, 0.100]\text{ s}$) to simulate dynamic 10–20 Hz telemetry rates.

---

<div align="center">
  <img src="assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>Protocol API Reference • SYNAPSE MOCK SERVER v1.2.0</i>
</div>
