from modelo import RegaloModel
from vista import RegaloView
from controlador import RegaloController

if __name__ == "__main__":
    modelo = RegaloModel()
    vista = RegaloView()
    controlador = RegaloController(modelo, vista)
    vista.mainloop()
