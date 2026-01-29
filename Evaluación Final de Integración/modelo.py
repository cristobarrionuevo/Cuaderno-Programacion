import sqlite3
import board
import adafruit_dht
import RPi.GPIO as GPIO
from datetime import datetime

class ModeloIncubadora:
    def __init__(self, dht_pin, led_pin):
        # Sensor DHT11
        self.sensor = adafruit_dht.DHT11(dht_pin)

        # LED
        self.led_pin = led_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, GPIO.LOW)

        # Base de datos
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self._crear_tabla()

    def _crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS incubadora (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                temperatura REAL,
                humedad REAL,
                fecha TEXT
            )
        """)
        self.conn.commit()

    def leer_sensor(self):
        try:
            temperatura = self.sensor.temperature
            humedad = self.sensor.humidity
            return temperatura, humedad
        except RuntimeError:
            return None, None

    def guardar_datos(self, temp, hum):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO incubadora (temperatura, humedad, fecha) VALUES (?, ?, ?)",
            (temp, hum, fecha)
        )
        self.conn.commit()

    def obtener_historial(self):
        self.cursor.execute(
            "SELECT temperatura, humedad, fecha FROM incubadora ORDER BY id DESC LIMIT 10"
        )
        return self.cursor.fetchall()

    def led_alerta_on(self):
        GPIO.output(self.led_pin, GPIO.HIGH)

    def led_alerta_off(self):
        GPIO.output(self.led_pin, GPIO.LOW)
