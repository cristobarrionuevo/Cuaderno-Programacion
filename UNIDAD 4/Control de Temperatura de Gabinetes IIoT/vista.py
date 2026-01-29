import time
import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class VistaSistema:
    def __init__(self, pin_azul, pin_rojo):
        self.pin_azul = pin_azul
        self.pin_rojo = pin_rojo
        self.error_activo = False

        GPIO.setup(pin_azul, GPIO.OUT)
        GPIO.setup(pin_rojo, GPIO.OUT)

        self.root = tk.Tk()
        self.root.title("Monitor IIoT")

        self.lbl_temp = tk.Label(self.root, text="Temperatura: -- °C", font=("Arial", 14))
        self.lbl_temp.pack()

        self.lbl_estado = tk.Label(self.root, text="Estado: NORMAL", width=30, bg="blue", fg="white")
        self.lbl_estado.pack(pady=5)

        self.lbl_error = tk.Label(self.root, text="", fg="red")
        self.lbl_error.pack()

        self.btn = tk.Button(self.root, text="Reintentar", command=self.reintentar, state="disabled")
        self.btn.pack(pady=10)

        self.root.update()

    def estado_normal(self, temp):
        GPIO.output(self.pin_azul, GPIO.HIGH)
        GPIO.output(self.pin_rojo, GPIO.LOW)
        self.lbl_temp.config(text=f"Temperatura: {temp} °C")
        self.lbl_estado.config(text="Estado: NORMAL", bg="blue")
        self.lbl_error.config(text="")
        self.btn.config(state="disabled")
        self.error_activo = False
        self.root.update()

    def estado_critico(self, mensaje):
        GPIO.output(self.pin_azul, GPIO.LOW)
        self.lbl_estado.config(text="Estado: CRÍTICO", bg="red")
        self.lbl_error.config(text=mensaje)
        self.btn.config(state="normal")
        self.error_activo = True

        for _ in range(6):
            GPIO.output(self.pin_rojo, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(self.pin_rojo, GPIO.LOW)
            time.sleep(0.3)

        self.root.update()

    def reintentar(self):
        self.lbl_estado.config(text="Estado: REINICIANDO", bg="orange")
        GPIO.output(self.pin_rojo, GPIO.LOW)
        self.error_activo = False
        self.root.update()

    def limpiar(self):
        GPIO.cleanup()
        self.root.destroy()
