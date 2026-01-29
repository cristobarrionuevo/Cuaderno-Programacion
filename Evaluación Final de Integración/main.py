import tkinter as tk
import board

from modelo import ModeloIncubadora
from vista import VistaIncubadora
from controlador import ControladorIncubadora

root = tk.Tk()

modelo = ModeloIncubadora(
    dht_pin=board.D27,  # GPIO 27
    led_pin=22          # GPIO 22
)

controlador = ControladorIncubadora(modelo, None)
vista = VistaIncubadora(root, controlador)
controlador.vista = vista

root.mainloop()
