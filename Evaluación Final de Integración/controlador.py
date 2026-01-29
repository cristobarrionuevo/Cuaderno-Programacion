class ControladorIncubadora:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        # Rangos recomendados de incubación
        self.TEMP_MIN = 36
        self.TEMP_MAX = 38

    def leer_sensor(self):
        temp, hum = self.modelo.leer_sensor()

        if temp is not None:
            self.vista.actualizar_datos(temp, hum)
            self.modelo.guardar_datos(temp, hum)
            self.actualizar_historial()

            # Lógica de alerta
            if temp < self.TEMP_MIN or temp > self.TEMP_MAX:
                self.modelo.led_alerta_on()
            else:
                self.modelo.led_alerta_off()

    def actualizar_historial(self):
        registros = self.modelo.obtener_historial()
        self.vista.mostrar_historial(registros)

    def encender_led(self):
        self.modelo.led_alerta_on()

    def apagar_led(self):
        self.modelo.led_alerta_off()
