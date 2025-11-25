import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)
    
    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)

class Boton:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
    
    def leer(self):
        return GPIO.input(self.pin)

class DHT11:
    # Sensor simulado
    def leer(self):
        temp = random.randint(20, 35)
        hum = random.randint(40, 80)
        return temp, hum