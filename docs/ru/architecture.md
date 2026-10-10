---
tags: [architecture, core, system, solid, grpc, client, simulation]
aliases: [Архитектура системы, Блупринт]
---

# 🏛️ SYNAPSE MOCK SERVER: Архитектура системы

В этом документе описывается внутренняя архитектура **SYNAPSE MOCK SERVER**, включая принципы SOLID и многопоточную модель взаимодействия с графическим интерфейсом Tkinter.

⬅️ Назад в [Центр документации](README.md) | ⚡ См. [Спецификацию API](api_reference.md)

---

## 1. Архитектурные слои

- **Слой представления:** Графический интерфейс Tkinter (`MockApp`) и `main.py`.
- **Слой абстракций:** Интерфейсы `ISynapseClient`, `IDataGenerator`, `FileParser`, `TopologyExtractor`, `TopologyQuerier`, `TopologyReporter`.
- **Слой инфраструктуры:** `GRPCClient`, `XMLParser` и фасад `TopologyAnalyzer`.
- **Домен симуляции:** Генератор реалистичного суточного трафика (`RealisticTrafficGenerator`) и случайный генератор (`RandomTrafficGenerator`).

---

## 2. Многопоточная модель

Потоковая передача кадров gRPC со скоростью 10–20 Гц выполняется в фоновом потоке-демоне (`daemon=True`). Вывод сообщений в консоль графического интерфейса планируется через `self.root.after(0, _update)` для обеспечения потокобезопасности Tkinter.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Архитектура</i>
</div>
