import requests
import RPi.GPIO as GPIO

# ===== CONFIGURACIÓN =====
TOKEN = "TU_TOKEN_DE_TELEGRAM"
CHAT_ID = "TU_CHAT_ID"

LED_VERDE = 17
LED_ROJO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_ROJO, GPIO.OUT)

# ===== VISTA =====
class VistaNotificacion:

    def enviar_telegram(self, mensaje):
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": mensaje}
        requests.post(url, data=data)

    def led_normal(self):
        GPIO.output(LED_VERDE, True)
        GPIO.output(LED_ROJO, False)

    def led_alarma(self):
        GPIO.output(LED_VERDE, False)
        GPIO.output(LED_ROJO, True)
