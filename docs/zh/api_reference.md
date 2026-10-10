---
tags: [api, grpc, reference, protobuf, hft]
aliases: [API 参考文档, Synapse 协议接口]
---

# ⚡ API 参考文档 & Synapse HFT 协议规范

本文档阐述 SYNAPSE MOCK SERVER 所使用的 `HFTLink` gRPC 服务接口规范 (`proto/synapse_hft.proto`)。

⬅️ 返回 [文档中心](README.md) | 🏛️ 查看 [系统架构](architecture.md)

---

## 1. gRPC 服务契约 `HFTLink`

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

- **`Ping`**: 心跳测试与服务端当前时间同步。
- **`LoadScenario`**: 传输压缩路网文件 `.net.xml.gz`、SHA-256 校验和及 ADAGIO 离线峰值时刻表。
- **`SystemControl`**: 下发系统控制指令 (`START`, `STOP` 等)。
- **`StreamTraffic`**: 客户端流式持续传输 `TrafficFrame` 交通流遥测数据帧。

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • API 参考</i>
</div>
