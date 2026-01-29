import random

class FalloHardwareError(Exception):
    def __init__(self, mensaje, pin):
        self.pin = pin
        super().__init__(f"{mensaje} | GPIO {pin}")

class SobrecalentamientoError(Exception):
    def __init__(self, mensaje, pin):
        self.pin = pin
        super().__init__(f"{mensaje} | GPIO {pin}")

class SensorTemperatura:
    def __init__(self, pin):
        self.pin = pin

    def leer_temperatura(self):
        # Simulación
        if random.choice([False, False, True]):
            return None
        return random.randint(30, 85)
