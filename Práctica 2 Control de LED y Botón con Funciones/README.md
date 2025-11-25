# Cuaderno-Programaci-n
📂 Práctica 2: Programación Modular con Funciones
**Archivo:** `script_funciones_gpio.py`

Evolución del código lineal a la **Programación Modular**. Se encapsularon las acciones del hardware en funciones para mejorar la organización.

* **Funcionalidad:** Control de LED y botón mejorado.
* **Mejoras:**
    * Uso de `def encender_led()` y `def apagar_led()`.
    * Implementación de resistencia `PULL_UP` interna para mejorar la lectura del botón.
    * Manejo de "Debounce" (anti-rebote) para evitar falsos contactos.