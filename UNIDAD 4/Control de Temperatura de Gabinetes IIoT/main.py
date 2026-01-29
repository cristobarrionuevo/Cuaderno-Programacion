from modelo import SensorTemperatura
from vista import VistaSistema
from controlador import ControladorTemperatura

PIN_SENSOR = 4
PIN_LED_AZUL = 17
PIN_LED_ROJO = 27

sensor = SensorTemperatura(PIN_SENSOR)
vista = VistaSistema(PIN_LED_AZUL, PIN_LED_ROJO)
controlador = ControladorTemperatura(sensor, vista)

controlador.ejecutar()
