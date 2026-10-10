---
tags: [architecture, core, system, solid, grpc, client, simulation]
aliases: [Arquitectura del Sistema, Arquitectura del Cliente]
---

# 🏛️ SYNAPSE MOCK SERVER: Arquitectura del Sistema

Este documento describe la arquitectura de software de **SYNAPSE MOCK SERVER**, detallando sus capas Clean Architecture, los principios SOLID en el análisis topológico y el modelo multihilo de la interfaz Tkinter.

⬅️ Volver al [Centro de Documentación](README.md) | ⚡ Ver [Referencia API](api_reference.md) | 🗺️ Ver [Análisis de Topología](topology_analysis.md)

---

## 1. Descomposición en Capas (Clean Architecture)

- **Capa de Presentación:** Interfaz Tkinter (`MockApp`) y script de entrada `main.py`.
- **Capa de Abstracciones:** Interfaces `ISynapseClient`, `IDataGenerator`, `FileParser`, `TopologyExtractor`, `TopologyQuerier` y `TopologyReporter`.
- **Capa de Infraestructura:** Implementaciones concretas `GRPCClient`, `XMLParser`, extractores, consultores y fachada `TopologyAnalyzer`.
- **Dominio de Simulación:** Generador realista diurno (`RealisticTrafficGenerator`) y generador aleatorio (`RandomTrafficGenerator`).

---

## 2. Principios SOLID en la Topología

1. **Responsabilidad Única (SRP):** Clases modulares para parseo, extracción, consulta y reporte.
2. **Abierto/Cerrado (OCP):** Soporte a nuevos formatos mediante `FileParser` sin alterar el código existente.
3. **Sustitución de Liskov (LSP):** Intercambiabilidad completa de implementaciones.
4. **Segregación de Interfaces (ISP):** Contratos pequeños y especializados.
5. **Inversión de Dependencias (DIP):** Inyección de dependencias en el constructor de `TopologyAnalyzer`.

---

## 3. Concurrencia y Despacho Seguro

Para evitar que la interfaz gráfica se congele durante la transmisión de telemetría a 10–20 Hz, el cliente gRPC se ejecuta en un hilo secundario daemon (`daemon=True`). Las actualizaciones de log en consola se envían de forma segura mediante `self.root.after(0, _update)`.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Arquitectura</i>
</div>
