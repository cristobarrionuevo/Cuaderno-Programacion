import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 18
BUTTON_PIN = 23

GPIO.setup(LED_PIN, GPIO.OUT)
# Nota: La línea siguiente se corta en la imagen, pero por lógica es GPIO.PUD_UP
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def encender_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

def apagar_led():
    GPIO.output(LED_PIN, GPIO.LOW)

def alternar_led(estado_actual):
    if estado_actual == 0:
        encender_led()
        return 1
    else:
        apagar_led()
        return 0

try:
    estado_led = 0
    boton_anterior = 1

    while True:
        lectura = GPIO.input(BUTTON_PIN)

        if lectura == 0 and boton_anterior == 1:
            estado_led = alternar_led(estado_led)
            time.sleep(0.2)
        
        boton_anterior = lectura
        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()