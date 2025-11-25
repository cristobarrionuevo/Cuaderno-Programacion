import RPi.GPIO as GPIO

class Dispositivo:
    def __init__(self, pin):
        self.pin = pin

class Led(Dispositivo):
    def __init__(self, pin):
        super().__init__(pin)
        GPIO.setup(self.pin, GPIO.OUT)
    
    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)

class Boton(Dispositivo):
    def __init__(self, pin):
        super().__init__(pin)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def presionado(self):
        return GPIO.input(self.pin) == GPIO.LOW