import random

# =========================
# Excepciones personalizadas
# =========================

class SensorOffline(Exception):
    def __init__(self, mensaje, id_sensor, codigo_error):
        super().__init__(mensaje)
        self.id_sensor = id_sensor
        self.codigo_error = codigo_error


class UmbralCritico(Exception):
    def __init__(self, mensaje, id_sensor, codigo_error):
        super().__init__(mensaje)
        self.id_sensor = id_sensor
        self.codigo_error = codigo_error


# =========================
# Función de monitoreo IIoT
# =========================

def monitorear_sensor(id_sensor):
    # Datos simulados aleatorios
    sensor_conectado = random.choice([True, True, True, False])
    valor_sensor = random.randint(20, 100)

    print(f"\n📡 Monitoreando sensor {id_sensor}")
    print(f"Conectado: {sensor_conectado}")
    print(f"Valor leído: {valor_sensor}")

    if not sensor_conectado:
        raise SensorOffline(
            "Sensor sin conexión",
            id_sensor,
            1001
        )

    if valor_sensor > 80:
        raise UmbralCritico(
            "Umbral crítico superado",
            id_sensor,
            2001
        )

    print(f"✅ Sensor {id_sensor} funcionando correctamente")


# =========================
# Ejecución principal
# =========================

try:
    monitorear_sensor("SENSOR-EDGE-01")

except SensorOffline as e:
    print("\n🚨 ERROR: SENSOR OFFLINE")
    print("ID del sensor:", e.id_sensor)
    print("Código de error:", e.codigo_error)
    print("Mensaje:", e)

except UmbralCritico as e:
    print("\n🔥 ALERTA: UMBRAL CRÍTICO")
    print("ID del sensor:", e.id_sensor)
    print("Código de error:", e.codigo_error)
    print("Mensaje:", e)

except Exception as e:
    print("\n❌ Error no controlado:", e)
