# vista.py
import tkinter as tk
import RPi.GPIO as GPIO

class EstadoView:
    def __init__(self, pin_led):
        self.pin_led = pin_led

        # GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_led, GPIO.OUT)

        # Tkinter
        self.root = tk.Tk()
        self.root.title("MVC Raspberry")
        self.root.geometry("300x200")

        self.lbl_estado = tk.Label(self.root, text="Estado: --", font=("Arial", 16))
        self.lbl_estado.pack(pady=15)

        self.btn_on = tk.Button(self.root, text="ON", width=10)
        self.btn_on.pack(pady=5)

        self.btn_off = tk.Button(self.root, text="OFF", width=10)
        self.btn_off.pack(pady=5)

        self.btn_toggle = tk.Button(self.root, text="TOGGLE", width=10)
        self.btn_toggle.pack(pady=5)

    def mostrar_estado(self, estado):
        self.lbl_estado.config(text=f"Estado: {estado}")
        if estado == "ON":
            GPIO.output(self.pin_led, GPIO.HIGH)
        else:
            GPIO.output(self.pin_led, GPIO.LOW)

    def iniciar(self):
        self.root.mainloop()

    def cerrar(self):
        GPIO.cleanup()
