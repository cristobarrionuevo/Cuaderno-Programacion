import tkinter as tk
from tkinter import ttk

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tk.Tk()
        self.ventana.title("Almacenamiento Seguro")
        self.ventana.geometry("420x320")

        ttk.Label(
            self.ventana,
            text="📦 Validador de Almacenamiento Seguro",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

        self.label_info = ttk.Label(
            self.ventana,
            text="Temperatura: -- °C\nHumedad: -- %",
            font=("Arial", 12)
        )
        self.label_info.pack(pady=10)

        ttk.Button(
            self.ventana,
            text="Verificar Ambiente",
            command=lambda: self.controlador.verificar_ambiente()
        ).pack(pady=10)

        self.label_estado = ttk.Label(
            self.ventana,
            text="",
            font=("Arial", 13, "bold")
        )
        self.label_estado.pack(pady=15)

    def mostrar_datos(self, temp, hum, seguro):
        self.label_info.config(
            text=f"Temperatura: {temp} °C\nHumedad: {hum} %"
        )

        if seguro:
            self.label_estado.config(
                text="✅ Ambiente seguro para almacenamiento",
                foreground="green"
            )
        else:
            self.label_estado.config(
                text="⚠️ Ambiente NO seguro",
                foreground="red"
            )

    def mostrar_error(self, mensaje):
        self.label_estado.config(
            text=f"🚨 ERROR: {mensaje}",
            foreground="red"
        )

    def iniciar(self):
        self.ventana.mainloop()
