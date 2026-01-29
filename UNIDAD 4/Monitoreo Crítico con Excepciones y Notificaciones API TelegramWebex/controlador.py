import time
from modelo import SensorTemperatura, SensorError, CriticalTempError
from vista import VistaNotificacion

# ===== CONTROLADOR =====
class ControladorSistema:
    def __init__(self):
        self.modelo = SensorTemperatura()
        self.vista = VistaNotificacion()

    def ejecutar(self):
        while True:
            try:
                temp, hum = self.modelo.leer_sensor()
                self.vista.led_normal()
                print(f"Temperatura: {temp}°C | Humedad: {hum}%")

            except CriticalTempError as e:
                self.vista.led_alarma()
                self.vista.enviar_telegram(
                    f"🔥 ALERTA CRÍTICA\nTemperatura: {e.temp}°C"
                )

            except SensorError as e:
                self.vista.enviar_telegram(f"❌ Error de sensor: {e}")

            except Exception as e:
                self.vista.enviar_telegram(f"⚠ Error inesperado: {e}")

            time.sleep(2)
