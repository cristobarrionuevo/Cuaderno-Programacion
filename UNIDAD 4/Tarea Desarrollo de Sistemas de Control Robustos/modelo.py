import adafruit_dht
import board

class ModeloAlmacenamiento:
    def __init__(self):
        self.dht = adafruit_dht.DHT11(board.D4)

    def leer_datos(self):
        temp = self.dht.temperature
        hum = self.dht.humidity

        # ASSERT 1: el sensor debe responder
        assert temp is not None and hum is not None, "Sensor sin respuesta"

        # ASSERT 2: rango lógico de temperatura
        assert -5 <= temp <= 50, "Temperatura fuera de rango seguro"

        # ASSERT 3: rango lógico de humedad
        assert 0 <= hum <= 100, "Humedad inválida"

        return temp, hum
