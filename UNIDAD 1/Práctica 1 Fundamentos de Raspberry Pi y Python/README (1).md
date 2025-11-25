# Cuaderno-Programaci-n
Práctica 1: Fundamentos de Raspberry Pi (GPIO Básico)
**Archivos:** `fundamentos_parpadeo.py`, `fundamentos_boton.py`

Introducción al hardware de la Raspberry Pi. El objetivo fue comprender cómo interactuar con los pines físicos y la diferencia entre los modos de numeración.

* **Conceptos Clave:**
    * **Modos de Pines (BCM vs BOARD):** Se aprendió a configurar la placa. `BCM` usa los números del chip Broadcom (ej. GPIO 18), mientras que `BOARD` usa el número físico del pin en la placa.
    * **Salidas Digitales (`GPIO.OUT`):** Script básico de parpadeo ("Hello World" en hardware) usando `time.sleep()`.
    * **Entradas Digitales (`GPIO.IN`):** Lectura de un pulsador físico mediante una estructura condicional `if/else` simple.

---