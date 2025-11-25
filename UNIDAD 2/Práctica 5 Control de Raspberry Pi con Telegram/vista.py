import telepot

class TelegramView:
    """Vista: se comunica con el usuario a través de Telegram"""
    
    def __init__(self, bot_token):
        self.telegram_bot = telepot.Bot(bot_token)

    def send_message(self, chat_id, message):
        """Envía un mensaje al usuario"""
        self.telegram_bot.sendMessage(chat_id, message)