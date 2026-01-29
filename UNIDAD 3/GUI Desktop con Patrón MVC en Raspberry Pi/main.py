# main.py
from modelo import EstadoModel
from vista import EstadoView
from controlador import EstadoController

PIN_LED = 17

def main():
    model = EstadoModel("estado.txt")
    view = EstadoView(PIN_LED)
    controller = EstadoController(model, view)
    view.iniciar()

if __name__ == "__main__":
    main()
