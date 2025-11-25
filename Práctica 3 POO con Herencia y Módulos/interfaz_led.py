import programa_led as led

def interfaz():
    while True:
        print("\n--- CONTROL DE LED ---")
        print("1. Modo BCM")
        print("2. Modo BOARD")
        print("3. Salir")

        modo = input("Selecciona modo: ")

        if modo == "3":
            break
        
        if modo == "1":
            pin_led, pin_boton = led.configurar_modo("BCM")
        elif modo == "2":
            pin_led, pin_boton = led.configurar_modo("BOARD")
        else:
            continue

        print("\n1. Parpadeo")
        print("2. Control botón")
        print("3. Volver")
        opcion = input("Elige: ")

        if opcion == "1":
            led.modo_parpadeo(pin_led)
        elif opcion == "2":
            led.modo_boton(pin_led, pin_boton)
        else:
            led.limpiar()

interfaz()