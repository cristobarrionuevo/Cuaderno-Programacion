import time
from model import Sensor, Notificador, SensorReadError, CriticalThresholdError
from view import Vista

TEMP_CRITICA = 28
TOKEN = "8535227713:AAFMaxvsBrdkoUD2xN0_X3IXiaPtVQkBg8k6659179297"
CHAT_ID = 6659179297


class Controlador:
    def __init__(self):
        self.sensor = Sensor()
        self.vista = Vista()
        self.notificador = Notificador(TOKEN, CHAT_ID)

    def ejecutar(self):
        try:
            while True:
                temp, hum = self.sensor.leer()

                if temp > TEMP_CRITICA:
                    raise CriticalThresholdError(
                        f"Temperatura crítica detectada: {temp}°C"
                    )

                self.vista.normal(temp)
                time.sleep(2)

        except CriticalThresholdError as e:
            self.vista.alerta(temp)
            self.notificador.enviar(str(e))

        except SensorReadError as e:
            print("❌ Error del sensor:", e)

        except KeyboardInterrupt:
            print("Programa detenido")

        finally:
            self.vista.limpiar()


if __name__ == "__main__":
    Controlador().ejecutar()

