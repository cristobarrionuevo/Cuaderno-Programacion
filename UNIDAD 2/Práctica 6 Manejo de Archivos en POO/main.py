import time
import telepot
from telepot.loop import MessageLoop
from controlador import Controlador

# ¡PON TU TOKEN DE TELEGRAM AQUÍ!
TOKEN = 'TU_TOKEN_DE_TELEGRAM'

bot = telepot.Bot(TOKEN)
controlador = Controlador(bot)

def handle(msg):
    controlador.manejar(msg)

MessageLoop(bot, handle).run_as_thread()
print('Bot escuchando...')

while True:
    time.sleep(10)