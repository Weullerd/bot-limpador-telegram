import asyncio
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TEMPO_APAGAR = 30  # segundos

async def apagar_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if not msg:
        return

    # log opcional pra debug
    print(f"Post recebido no canal: {msg.message_id}")

    await asyncio.sleep(TEMPO_APAGAR)

    try:
        await context.bot.delete_message(
            chat_id=msg.chat_id,
            message_id=msg.message_id
        )
        print(f"Post {msg.message_id} apagado")
    except Exception as e:
        print(f"Erro ao apagar post {msg.message_id}: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handler correto para posts em CANAIS
app.add_handler(
    MessageHandler(filters.ChatType.CHANNEL, apagar_posts)
)

print("🤖 Bot limpador rodando...")
app.run_polling()
