# 🐍🪜 Serpientes y Escaleras (Python) — TP UBA

Implementación en **Python** del clásico **Serpientes y Escaleras**, con mejoras de jugabilidad, **casilleros especiales aleatorios** y un sistema de **estadísticas** para analizar el comportamiento de la partida.

> Proyecto académico desarrollado para practicar lógica de programación, estructuras de datos y diseño modular.

---

## ✨ Características principales

🎮 **Juego para 2 jugadores** por turnos desde consola.  
🧩 **Tablero ASCII** con estética y mensajes de estado.  
🐍🪜 **Serpientes y escaleras** (mapeo de posiciones) para avanzar/retroceder según el casillero.  
🍌 **Casilleros especiales aleatorios** (generados sin superponerse con serpientes/escaleras):
- 🍌 *Cáscara de banana*: retrocede 2 “pisos”
- 🪄 *Mágico*: teletransporte a un casillero aleatorio
- ⚡ *Rushero*: avanza al final del piso (múltiplo de 10)
- 🍄 *Hongos locos*: retrocede al inicio del piso

📊 **Estadísticas de partida**
- Conteo de caídas en cada tipo de casillero especial
- Conteo de encuentros con serpientes y escaleras  
♻️ **Reset de estadísticas** desde el menú

---

## 🧠 Conceptos aplicados

✅ Estructuras de datos: `dict`, `list` y control de estados  
✅ Modularización mediante funciones y responsabilidades separadas  
✅ Generación aleatoria controlada (sin colisiones de casilleros)  
✅ Validaciones de input y flujo por menú  
✅ Tracking/telemetría simple (contadores de eventos)

---

## ▶️ Cómo ejecutar

Requisitos:
- Python 3.x

Ejecutar:
```bash
python "TP1 Serpientes y Escaleras.py"
