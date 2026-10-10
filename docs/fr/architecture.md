---
tags: [architecture, core, system, solid, grpc, client, simulation]
aliases: [Architecture du Système, Blueprint]
---

# 🏛️ SYNAPSE MOCK SERVER: Architecture du Système

Ce document décrit l'architecture logicielle de **SYNAPSE MOCK SERVER**, son modèle multi-thread et l'application des principes SOLID.

⬅️ Retour au [Hub de Documentation](README.md) | ⚡ Voir [Référence API](api_reference.md) | 🗺️ Voir [Topologie](topology_analysis.md)

---

## 1. Décomposition en Couches

- **Couche Présentation:** Interface Tkinter (`MockApp`) et script `main.py`.
- **Couche Abstraction:** Interfaces `ISynapseClient`, `IDataGenerator`, `FileParser`, `TopologyExtractor`, `TopologyQuerier`, `TopologyReporter`.
- **Couche Infrastructure:** `GRPCClient`, `XMLParser` et façade `TopologyAnalyzer`.
- **Domaine Simulation:** `RealisticTrafficGenerator` et `RandomTrafficGenerator`.

---

## 2. Principes SOLID et Concurrence

La transmission gRPC en flux continu (10–20 Hz) s'exécute dans un thread d'arrière-plan (`daemon=True`). Les mises à jour de l'interface graphique Tkinter sont ordonnancées de manière thread-safe via `self.root.after(0, _update)`.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Architecture</i>
</div>
