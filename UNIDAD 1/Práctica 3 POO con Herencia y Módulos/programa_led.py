import RPi.GPIO as GPIO
import time

def configurar_modo(modo):
    if modo == "BCM":
        GPIO.setmode(GPIO.BCM)
        pin_led = 18
        pin_boton = 23
    elif modo == "BOARD":
        GPIO.setmode(GPIO.BOARD)
        pin_led = 12
        pin_boton = 16
    
    GPIO.setup(pin_led, GPIO.OUT)
    GPIO.setup(pin_boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    return pin_led, pin_boton

def modo_parpadeo(pin_led):
    try:
        while True:
            GPIO.output(pin_led, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pin_led, GPIO.LOW)
            time.sleep(0.5)
    except KeyboardInterrupt:
        limpiar()

def modo_boton(pin_led, pin_boton):
    try:
        while True:
            if GPIO.input(pin_boton) == GPIO.LOW:
                GPIO.output(pin_led, GPIO.HIGH)
            else:
                GPIO.output(pin_led, GPIO.LOW)
            time.sleep(0.1)
    except KeyboardInterrupt:
        limpiar()

def limpiar():
    GPIO.cleanup()