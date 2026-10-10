---
tags: [architecture, core, system, solid, grpc, client, simulation]
aliases: [系统架构, 系统蓝图]
---

# 🏛️ SYNAPSE MOCK SERVER: 系统架构蓝图

本文档深入解析 **SYNAPSE MOCK SERVER** 的内部软件架构、SOLID 重构设计及多线程桌面并发模型。

⬅️ 返回 [文档中心](README.md) | ⚡ 查看 [API 参考](api_reference.md)

---

## 1. 清洁分层架构 (Clean Architecture)

- **表现层:** Tkinter 桌面控制台 (`MockApp`) 与启动脚本 `main.py`。
- **抽象层:** `ISynapseClient`, `IDataGenerator`, `FileParser`, `TopologyExtractor`, `TopologyQuerier`, `TopologyReporter` 抽象接口。
- **基础设施层:** `GRPCClient`, `XMLParser` 以及拓扑外观门面 `TopologyAnalyzer`。
- **仿真域:** 现实日夜周期交通流生成器 (`RealisticTrafficGenerator`) 与随机游走生成器 (`RandomTrafficGenerator`)。

---

## 2. 多线程与线程安全调度

为确保在高频 gRPC 推流（10–20 Hz）期间 Tkinter 界面保持高响应度，数据流生成与网络传输均在后台守护线程 (`daemon=True`) 中运行。界面日志更新通过 `self.root.after(0, _update)` 派发至主线程事件循环，严格遵循线程安全标准。

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • 架构设计</i>
</div>
