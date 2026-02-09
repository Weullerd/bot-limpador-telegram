import asyncio
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN") or "8462336015:AAHWg_thwvm6n3A2StpJ8iqUIM669NFeFGA"
TEMPO_APAGAR = 30  # segundos

async def apagar_bots(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg:
        return

    # Apaga SOMENTE mensagens enviadas por bots
    if msg.from_user and msg.from_user.is_bot:
        await asyncio.sleep(TEMPO_APAGAR)
        await msg.delete()

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Isso aqui substitui o ChannelPostHandler
app.add_handler(MessageHandler(filters.ChatType.CHANNEL, apagar_bots))

print("🤖 Bot limpador rodando...")
app.run_polling()