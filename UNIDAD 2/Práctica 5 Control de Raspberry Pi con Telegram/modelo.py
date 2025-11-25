import RPi.GPIO as GPIO

class LEDModel:
    """Modelo que maneja el estado del LED físico"""
    
    def __init__(self, led_pin):
        self.led_pin = led_pin
        
        # Configuración inicial
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.led_pin, GPIO.OUT)
        
        # Iniciar apagado
        GPIO.output(self.led_pin, 0)

    def turn_on(self):
        """Enciende el LED"""
        GPIO.output(self.led_pin, 1)

    def turn_off(self):
        """Apaga el LED"""
        GPIO.output(self.led_pin, 0)