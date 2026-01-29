import adafruit_dht
import board

# ===== EXCEPCIONES PERSONALIZADAS =====
class SensorError(Exception):
    pass

class CriticalTempError(SensorError):
    def __init__(self, temp, mensaje="⚠ Temperatura crítica detectada"):
        self.temp = temp
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# ===== MODELO =====
class SensorTemperatura:
    def __init__(self):
        self.sensor = adafruit_dht.DHT11(board.D4)

    def leer_sensor(self):
        try:
            temperatura = self.sensor.temperature
            humedad = self.sensor.humidity

            if temperatura is None:
                raise SensorError("Lectura inválida del sensor")

            if temperatura >= 35:
                raise CriticalTempError(temperatura)

            return temperatura, humedad

        except RuntimeError:
            raise SensorError("Error de lectura del DHT")
