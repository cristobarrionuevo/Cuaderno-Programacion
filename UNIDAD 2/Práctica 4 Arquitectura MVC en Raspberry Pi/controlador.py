from modelo.dispositivos import Led, Boton, DHT11
from vista.consola import mostrar_estado, mostrar_dht
import time

led = Led(18)
boton = Boton(23)
sensor = DHT11()

try:
    while True:
        # LED controlado por botón
        if boton.leer() == 1:
            led.encender()
            mostrar_estado("LED encendido")
        else:
            led.apagar()
            mostrar_estado("LED apagado")
        
        # Lectura del DHT11
        temp, hum = sensor.leer()
        mostrar_dht(temp, hum)

        time.sleep(2)

except KeyboardInterrupt:
    print("Finalizando programa...")