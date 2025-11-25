import time
import telepot
from telepot.loop import MessageLoop
from modelo import RobotConstructor, RobotMedico, RobotExplorador, guardar_dato
from vista import TelegramView
import RPi.GPIO as GPIO

class Controlador:
    def __init__(self, bot):
        self.bot = bot
        self.vista = TelegramView()

        self.constructor = RobotConstructor("Constructor")
        self.medico = RobotMedico("Medico")
        self.explorador = RobotExplorador("Explorador")

    def manejar(self, msg):
        chat_id = msg["chat"]["id"]
        comando = msg["text"]

        if comando == "/start":
            self.vista.enviar(self.bot, chat_id, self.vista.menu())
        
        elif comando == "/constructor_on":
            self.vista.enviar(self.bot, chat_id, self.constructor.encender())
            
        elif comando == "/constructor_off":
            self.vista.enviar(self.bot, chat_id, self.constructor.apagar())
            
        elif comando == "/medico_temp":
            self.vista.enviar(self.bot, chat_id, self.medico.medir_temperatura())
            
        elif comando == "/medico_hum":
            self.vista.enviar(self.bot, chat_id, self.medico.medir_humedad())
            
        elif comando == "/explorar":
            self.vista.enviar(self.bot, chat_id, "Presiona el botón para detener exploración...")
            # Nota: Esto bloqueará el bot hasta que presiones el botón físico
            resultado = self.explorador.explorar()
            self.vista.enviar(self.bot, chat_id, resultado)