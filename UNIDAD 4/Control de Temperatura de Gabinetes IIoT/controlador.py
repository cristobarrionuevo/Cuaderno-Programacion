import time
from modelo import FalloHardwareError, SobrecalentamientoError

class ControladorTemperatura:
    def __init__(self, sensor, vista):
        self.sensor = sensor
        self.vista = vista

    def ejecutar(self):
        while True:  # 🔁 BUCLE OBLIGATORIO
            try:
                if self.vista.error_activo:
                    self.vista.root.update()
                    time.sleep(0.5)
                    continue

                temp = self.sensor.leer_temperatura()

                if temp is None:
                    raise FalloHardwareError("Fallo de hardware: sensor no responde", self.sensor.pin)

                if temp > 70:
                    raise SobrecalentamientoError(f"Sobrecalentamiento: {temp} °C", self.sensor.pin)

                self.vista.estado_normal(temp)
                time.sleep(2)

            except FalloHardwareError as e:
                self.vista.estado_critico(str(e))

            except SobrecalentamientoError as e:
                self.vista.estado_critico(str(e))

            finally:
                self.vista.root.update()
