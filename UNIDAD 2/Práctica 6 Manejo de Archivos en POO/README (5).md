# Cuaderno-Programaci-n
Práctica 6 (Proyecto Final): Manejo de Archivos y Robots

Sistema avanzado que utiliza un solo LED  para representar diferentes "Robots" y guarda automáticamente todo lo que hacen en archivos de texto.

* **Roles de los Robots:**
    * `RobotConstructor`: Control manual del LED (Prender/Apagar).
    * `RobotMedico`: Lee la temperatura y humedad real del ambiente.
    * `RobotExplorador`: Mide cuánto tiempo tardas en presionar el botón para detener una "exploración".
* **Guardado de Datos (Logs):**
    * El programa crea automáticamente los archivos `log_acciones.txt` y `log_sensor.txt`.
    * Cada vez que usas un robot, se queda guardada la fecha, la hora y el dato (temperatura o tiempo) para que no se pierda.