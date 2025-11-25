import time
import telepot
from telepot.loop import MessageLoop
from modelo import LEDModel 
from vista import TelegramView

class LEDController:
    """Controlador: une al modelo (LED) y la vista (Telegram)"""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process_command(self, chat_id, command):
        """Procesa los mensajes que llegan desde Telegram"""
        command = command.lower()

        if "on" in command and "led" in command:
            self.model.turn_on()
            self.view.send_message(chat_id, "💡 LED encendido")
        
        elif "off" in command and "led" in command:
            self.model.turn_off()
            self.view.send_message(chat_id, "🌑 LED apagado")
        
        else:
            self.view.send_message(chat_id, "Comando no reconocido. Use 'on led' o 'off led'.")


if __name__ == "__main__":

    BOT_TOKEN = "5535227713:AAF8nsvxRcDrC0XW0_RIXX1eP67Q4RgoK" 
    LED_PIN = 18

    modelo = LEDModel(LED_PIN)
    vista = TelegramView(BOT_TOKEN)
    controlador = LEDController(modelo, vista)

    def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']
        print(f"Recibido: {command}")
        
        controlador.process_command(chat_id, command)

    MessageLoop(vista.telegram_bot, handle).run_as_thread()
    print("Bot escuchando... (Presiona Ctrl+C para salir)")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        GPIO.cleanup()