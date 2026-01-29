import adafruit_dht
import board
import telepot

# ===== Excepciones =====
class SensorReadError(Exception):
    pass

class CriticalThresholdError(Exception):
    pass


class Sensor:
    def __init__(self):
        # DHT11 con adafruit_dht (MINÚSCULA)
        self.dht = adafruit_dht.DHT11(board.D4)

    def leer(self):
        try:
            temperatura = self.dht.temperature
            humedad = self.dht.humidity

            if temperatura is None or humedad is None:
                raise SensorReadError("Lectura inválida del DHT11")

            # Validación obligatoria
            assert 0 <= humedad <= 100, "Humedad fuera de rango"

            return temperatura, humedad

        except AssertionError as e:
            raise SensorReadError(e)

        except Exception as e:
            raise SensorReadError(e)


class Notificador:
    def __init__(self, token, chat_id):
        if not token:
            raise ValueError("Token de Telegram nulo")

        self.bot = telepot.Bot(token)
        self.chat_id = chat_id

    def enviar(self, mensaje):
        self.bot.sendMessage(self.chat_id, mensaje)
