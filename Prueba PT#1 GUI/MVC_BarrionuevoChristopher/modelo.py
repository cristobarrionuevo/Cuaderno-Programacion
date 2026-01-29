class RegaloModel:
    """
    Modelo:
    Maneja únicamente los datos de la aplicación.
    No tiene ninguna referencia a Tkinter.
    """
    def __init__(self):
        self.regalos = []

    def agregar_regalo(self, regalo):
        self.regalos.append(regalo)

    def obtener_regalos(self):
        return self.regalos
