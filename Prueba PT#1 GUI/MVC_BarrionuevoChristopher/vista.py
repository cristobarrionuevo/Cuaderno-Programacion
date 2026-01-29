import tkinter as tk
from tkinter import ttk

class RegaloView(tk.Tk):
    """
    Vista:
    Contiene solo la interfaz gráfica (GUI).
    """
    def __init__(self):
        super().__init__()

        self.title("Lista de Regalos MVC")
        self.geometry("350x350")
        self.resizable(False, False)

        # Entrada de regalo
        self.lbl_input = tk.Label(self, text="Regalo:")
        self.lbl_input.pack(pady=5)

        self.entry_regalo = tk.Entry(self)
        self.entry_regalo.pack(pady=5)

        # ComboBox
        self.lbl_combo = tk.Label(self, text="Para:")
        self.lbl_combo.pack(pady=5)

        self.combo_destino = ttk.Combobox(
            self,
            values=["Hermanos", "Padres", "Amigos"],
            state="readonly"
        )
        self.combo_destino.current(0)
        self.combo_destino.pack(pady=5)

        # Botón
        self.btn_agregar = tk.Button(
            self,
            text="Agregar a la Bolsa",
            bg="white",
            fg="black"
        )
        self.btn_agregar.pack(pady=10)

        # Listbox
        self.listbox = tk.Listbox(self, width=40)
        self.listbox.pack(pady=10)
