import RPi.GPIO as GPIO

LED_OK = 17
LED_ERROR = 27

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_OK, GPIO.OUT)
        GPIO.setup(LED_ERROR, GPIO.OUT)

    def verificar_ambiente(self):
        try:
            temp, hum = self.modelo.leer_datos()

            # Ambiente considerado seguro
            ambiente_seguro = (10 <= temp <= 30) and (30 <= hum <= 70)

            if ambiente_seguro:
                GPIO.output(LED_OK, GPIO.HIGH)
                GPIO.output(LED_ERROR, GPIO.LOW)
            else:
                GPIO.output(LED_OK, GPIO.LOW)
                GPIO.output(LED_ERROR, GPIO.HIGH)

            self.vista.mostrar_datos(temp, hum, ambiente_seguro)

        except AssertionError as e:
            GPIO.output(LED_OK, GPIO.LOW)
            GPIO.output(LED_ERROR, GPIO.HIGH)
            self.vista.mostrar_error(str(e))
