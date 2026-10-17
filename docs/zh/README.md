<div align="center">

# SYNAPSE MOCK SERVER — 技术文档中心
### 高频遥测测试基准与交通流仿真引擎
*Noxfort Systems — A State Of Art Company*

[![状态](https://img.shields.io/badge/状态-活跃-brightgreen?style=flat&logo=github)](https://github.com/Noxfort-Systems-Brazil/Synapse_Mock_Server)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![gRPC](https://img.shields.io/badge/gRPC-v1.62%2B-244c5a?style=flat&logo=grpc&logoColor=white)](https://grpc.io/)
[![Protocol Buffers](https://img.shields.io/badge/Protobuf-v4.25%2B-blue?style=flat)](https://protobuf.dev/)
[![SPDX 开源协议](https://img.shields.io/badge/SPDX--License--Identifier-Apache--2.0-blue.svg)](../../LICENSE)


---

### 🌐 语言选择

[**🇺🇸 English**](../en/README.md) • [**🇧🇷 Português (Brasil)**](../pt-br/README.md) • [**🇪🇸 Español**](../es/README.md) • [**🇫🇷 Français**](../fr/README.md) • [**🇷🇺 Русский**](../ru/README.md) • [**🇨🇳 简体中文**](README.md)

---

</div>

欢迎查阅 **SYNAPSE MOCK SERVER** 中文技术文档。

**SYNAPSE MOCK SERVER** 是 CARINA 智能交通生态系统的官方客户端测试平台与高频遥测（HFT）仿真器。系统基于 **Clean Architecture** 和 **SOLID** 设计原则构建，提供高吞吐量 gRPC 实时数据推流，用于智能信号控制算法和数字孪生系统的压力测试与仿真基准验证。

---

## 📚 核心技术模块

- **[系统架构与分层设计](architecture.md)**: 清洁架构、SOLID 原则与桌面多线程模型。
- **[Synapse HFT API 参考](api_reference.md)**: `HFTLink` gRPC 接口与 Protobuf 消息规范。
- **[SUMO 路网拓扑分析](topology_analysis.md)**: `.net.xml.gz` 格式解析与上下游图查询。
- **[自动化测试与质量保障](testing.md)**: 单元测试执行与 SOLID 接口 Mock 规范。

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • 中文技术文档</i><br/>
  <small>遵循 <a href="../../LICENSE">Apache 2.0</a> 开源许可协议 (SPDX-License-Identifier: <code>Apache-2.0</code>)。© 2026 Gabriel Moraes - Noxfort Systems。</small>
</div>

