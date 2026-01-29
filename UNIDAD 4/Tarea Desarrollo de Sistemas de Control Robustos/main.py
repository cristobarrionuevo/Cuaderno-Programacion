from modelo import ModeloAlmacenamiento
from controlador import Controlador
from view import Vista

def main():
    modelo = ModeloAlmacenamiento()
    vista = Vista(None)
    controlador = Controlador(modelo, vista)
    vista.controlador = controlador
    vista.iniciar()

if __name__ == "__main__":
    main()
