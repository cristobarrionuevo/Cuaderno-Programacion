# controlador.py
class EstadoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Estado inicial
        self.view.mostrar_estado(self.model.estado)

        # Eventos botones
        self.view.btn_on.config(command=self.encender)
        self.view.btn_off.config(command=self.apagar)
        self.view.btn_toggle.config(command=self.toggle)

    def encender(self):
        self.model.encender()
        self.view.mostrar_estado(self.model.estado)

    def apagar(self):
        self.model.apagar()
        self.view.mostrar_estado(self.model.estado)

    def toggle(self):
        self.model.toggle()
        self.view.mostrar_estado(self.model.estado)
