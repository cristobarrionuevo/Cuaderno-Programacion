import RPi.GPIO as GPIO

class Vista:
    LED_ROJO = 17
    LED_VERDE = 27

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.LED_ROJO, GPIO.OUT)
        GPIO.setup(self.LED_VERDE, GPIO.OUT)

    def normal(self, temp):
        GPIO.output(self.LED_ROJO, GPIO.LOW)
        GPIO.output(self.LED_VERDE, GPIO.HIGH)
        print(f"✅ Temperatura normal: {temp}°C")

    def alerta(self, temp):
        GPIO.output(self.LED_VERDE, GPIO.LOW)
        GPIO.output(self.LED_ROJO, GPIO.HIGH)
        print(f"🚨 TEMPERATURA CRÍTICA: {temp}°C")

    def limpiar(self):
        GPIO.cleanup()




