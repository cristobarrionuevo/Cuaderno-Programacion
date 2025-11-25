class TelegramView:
    def enviar(self, bot, chat_id, mensaje):
        bot.sendMessage(chat_id, mensaje)

    def menu(self):
        return """
        🤖 COMANDOS DISPONIBLES:
        
        💡 CONTROL MANUAL:
        /constructor_on  - Encender LED
        /constructor_off - Apagar LED
        
        🌡️ SENSOR DHT11:
        /medico_temp     - Ver Temperatura
        /medico_hum      - Ver Humedad
        
        🚀 AUTOMATIZACIÓN:
        /explorar        - Iniciar modo exploración
        """