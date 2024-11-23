from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import requests
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
URL_MICROSERVICIO = 'http://localhost:8000/run_agent'


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy bot de pedidos, en que puedo ayudarte?")
    

async def manejar_mensaje(update: Update, context: CallbackContext):
    mensaje_usuario = update.message.text
    id_usuario = update.message.from_user.id
    print(update.message.from_user)

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    datos = {
        "message": mensaje_usuario,
        "id": id_usuario
        }
    requests.post(URL_MICROSERVICIO, json=datos)


def main():

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    app.run_polling()


if __name__ == '__main__':
    main()
