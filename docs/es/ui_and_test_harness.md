---
tags: [ui, dashboard, tkinter, test_harness, threads]
aliases: [Interfaz Gráfica, Panel de Pruebas Tkinter]
---

# 🖥️ Interfaz Gráfica & Banco de Pruebas Desktop

Este documento detalla la aplicación de escritorio Tkinter (`MockApp`) en SYNAPSE MOCK SERVER, abordando su diseño multihilo y consola de eventos.

⬅️ Volver al [Centro de Documentación](README.md) | 🏛️ Ver [Arquitectura](architecture.md) | ⚡ Ver [API](api_reference.md)

---

## 1. Diseño y Controles de la Interfaz

- **Selector de Mapa:** Abre el diálogo de búsqueda para archivos comprimidos `.net.xml.gz`.
- **Botón `▶ Play`:** Inicia el parseo del mapa y arranca el hilo de transmisión gRPC en segundo plano.
- **Botón `Stop`:** Detiene el flujo de tramas y restablece los controles.
- **Consola Oscura de Logs:** Área de texto con fondo oscuro (`#1e1e1e`) para inspección en tiempo real.
- **Despacho Seguro:** Registro thread-safe en el widget de Tkinter mediante `self.root.after(0, _update)`.

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Interfaz de Usuario</i>
</div>
