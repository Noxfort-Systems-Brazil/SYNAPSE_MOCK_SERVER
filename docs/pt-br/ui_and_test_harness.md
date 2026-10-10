---
tags: [ui, dashboard, tkinter, test_harness, threads]
aliases: [Interface Gráfica, Painel Desktop, Harness Tkinter]
---

# 🖥️ Interface Gráfica & Painel de Testes Tkinter

Este documento aborda a arquitetura da interface desktop **`MockApp`**, incluindo os componentes visuais, o ciclo de vida do streaming e o console de mensagens assíncrono.

⬅️ Voltar para o [Hub de Documentação](synapse_mock_moc.md) | 🏛️ Ver [Arquitetura](architecture.md) | ⚡ Ver [API](api_reference.md)

---

## 1. Componentes do Painel

A aplicação desktop construída em Tkinter (`ui/app_ui.py`) possui os seguintes módulos de tela:

1. **Painel de Seleção de Mapa:** Exibe o arquivo atual e abre o seletor para arquivos compactados do SUMO (`*.net.xml.gz`).
2. **Botões de Controle:**
   - `▶ Play`: Valida o mapa selecionado, extrai a lista de arestas e inicia a thread de streaming.
   - `Stop`: Interrompe a transmissão e restaura os botões.
3. **Console Escuro de Logs:** Área de texto estilo terminal (`bg="#1e1e1e"`, `fg="#d4d4d4"`) com rolagem automática e timestamp para cada evento registrado.
4. **Barra de Status:** Exibe informações de conexão, tentativas de reconexão e contagem de arestas ativas.

---

## 2. Threading e Atualização Segura do Console

O envio de telemetria gRPC a 10–20 Hz é executado em uma thread separada (`threading.Thread(target=self._run_simulation, daemon=True)`) para não bloquear a interface gráfica.

Como o Tkinter não permite que threads secundárias manipulem componentes gráficos diretamente, as mensagens de log são encaminhadas via `self.root.after(0, _update)`:

```python
def log(self, message):
    timestamp = time.strftime("%H:%M:%S")
    full_message = f"[{timestamp}] {message}\n"
    print(full_message.strip())
    
    def _update():
        self.log_area.config(state="normal")
        self.log_area.insert(tk.END, full_message)
        self.log_area.see(tk.END)
        self.log_area.config(state="disabled")
    
    # Agenda a atualização na fila de eventos da thread principal
    self.root.after(0, _update)
```

---

<div align="center">
  <img src="../assets/noxfort-logo.png" alt="Noxfort Systems Logo" width="45" /><br/>
  <b>Noxfort Systems</b> — <i>A State Of Art Company</i><br/>
  <i>SYNAPSE MOCK SERVER v1.2.0 • Interface Desktop</i>
</div>
