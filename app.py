import os, logging
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    while True:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá mundo! Eu sou o bot de jogos grátis!")
        time.sleep(5)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("API_TOKEN")).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()