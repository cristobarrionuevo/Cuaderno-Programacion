import RPi.GPIO as GPIO
import time
from dispositivos import Led, Boton

GPIO.setmode(GPIO.BCM)

led = Led(18)
boton = Boton(23)

try:
    while True:
        if boton.presionado():
            led.encender()
        else:
            led.apagar()
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()