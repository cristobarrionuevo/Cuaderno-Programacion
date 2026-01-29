import tkinter as tk

class RegaloController:
    """
    Controlador:
    Conecta el Modelo y la Vista.
    Contiene la lógica de la aplicación.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Conectar botón con método
        self.view.btn_agregar.config(command=self.agregar_regalo)

    def agregar_regalo(self):
        regalo = self.view.entry_regalo.get()
        destino = self.view.combo_destino.get()

        if regalo != "":
            texto = f"{regalo} para {destino}"
            self.model.agregar_regalo(texto)
            self.actualizar_lista()
            self.limpiar_campos()

    def actualizar_lista(self):
        self.view.listbox.delete(0, tk.END)
        for r in self.model.obtener_regalos():
            self.view.listbox.insert(tk.END, r)

    def limpiar_campos(self):
        self.view.entry_regalo.delete(0, tk.END)
        self.view.combo_destino.current(0)
