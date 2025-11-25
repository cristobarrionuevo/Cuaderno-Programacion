import RPi.GPIO as GPIO
import time
import adafruit_dht
import board

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# --- CONFIGURACIÓN PARA UN SOLO LED ---
# Usamos el mismo pin (18) para ambas variables
PIN_LED_UNICO = 18 
PIN_LED_CONSTRUCTOR = PIN_LED_UNICO
PIN_LED_EXPLORADOR  = PIN_LED_UNICO

PIN_BOTON = 25
PIN_SENSOR = board.D4 

GPIO.setup(PIN_LED_UNICO, GPIO.OUT) # Solo configuramos uno
GPIO.setup(PIN_BOTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Variables Globales
contador_constructor_on = 0
contador_explorador_veces = 0
contador_boton_presionado = 0
tiempo_exploracion_total = 0.0
ultima_temperatura = None
ultima_humedad = None

dht_device = adafruit_dht.DHT11(PIN_SENSOR)

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre

class RobotConstructor(Robot):
    def encender(self):
        global contador_constructor_on
        contador_constructor_on += 1
        GPIO.output(PIN_LED_CONSTRUCTOR, True)
        guardar_dato("led_constructor", "log_acciones.txt")
        return f"{self.nombre}: LED Encendido"

    def apagar(self):
        GPIO.output(PIN_LED_CONSTRUCTOR, False)
        return f"{self.nombre}: LED Apagado"

class RobotMedico(Robot):
    def medir_temperatura(self):
        global ultima_temperatura
        try:
            ultima_temperatura = dht_device.temperature
            guardar_dato("temperatura", "log_sensor.txt")
            return f"{self.nombre}: Temperatura {ultima_temperatura}°C"
        except RuntimeError:
            return f"{self.nombre}: Reintentando lectura..."

    def medir_humedad(self):
        global ultima_humedad
        try:
            ultima_humedad = dht_device.humidity
            guardar_dato("humedad", "log_sensor.txt")
            return f"{self.nombre}: Humedad {ultima_humedad}%"
        except RuntimeError:
            return f"{self.nombre}: Reintentando lectura..."

class RobotExplorador(Robot):
    def explorar(self):
        global contador_explorador_veces, tiempo_exploracion_total, contador_boton_presionado
        
        contador_explorador_veces += 1
        
        # Encendemos el MISMO led
        GPIO.output(PIN_LED_EXPLORADOR, True)
        inicio = time.time()
        
        print("Esperando botón para detener exploración...")
        while GPIO.input(PIN_BOTON) == GPIO.LOW:
            time.sleep(0.1)
        
        contador_boton_presionado += 1
        fin = time.time()
        tiempo_exploracion_total += (fin - inicio)
        
        GPIO.output(PIN_LED_EXPLORADOR, False)
        
        guardar_dato("explorador", "log_acciones.txt")
        guardar_dato("tiempo", "log_acciones.txt")
        
        return f"{self.nombre}: Exploración finalizada. Tiempo: {round(fin-inicio, 2)}s"

def guardar_dato(tipo, archivo):
    # (El resto de esta función de guardado se mantiene igual que antes)
    global contador_constructor_on, contador_explorador_veces, contador_boton_presionado
    global tiempo_exploracion_total, ultima_temperatura, ultima_humedad

    datos = {
        "led_constructor": f"Constructor encendió LED: {contador_constructor_on} veces",
        "explorador": f"Exploración iniciada: {contador_explorador_veces} veces",
        "boton": f"Botón detenido: {contador_boton_presionado} veces",
        "tiempo": f"Tiempo acumulado explorando: {tiempo_exploracion_total:.2f} s",
        "temperatura": f"Temp: {ultima_temperatura}°C",
        "humedad": f"Hum: {ultima_humedad}%"
    }

    try:
        with open(archivo, "a") as f:
            if tipo in datos:
                f.write(datos[tipo] + "\n")
                return "Dato guardado."
    except:
        return "Error guardando."