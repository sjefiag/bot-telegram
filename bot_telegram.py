
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Token del bot
TOKEN = "7579069473:AAEEV6IWG8KNAyloEm8LGQNyZ8CWu5y_Tb0"
# ID del grupo
GROUP_ID = -1001415553766

# Función que recibe mensajes
async def handle_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    if chat_id == GROUP_ID:
        print(f"Mensaje recibido en el grupo: {text}")

# Configurar el bot
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot escuchando mensajes en el grupo...")
    app.run_polling()

if __name__ == "__main__":
    main()
