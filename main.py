
import os
import requests
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً بك في بوت WhaleTap!")

async def whales(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("جاري البحث عن صفقات الحيتان...")

    url = f"https://api.helius.xyz/v0/addresses?api-key={HELIUS_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            await update.message.reply_text(f"عدد المحافظ: {len(result)}")
        else:
            await update.message.reply_text("فشل في جلب البيانات من Helius.")
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {str(e)}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("whales", whales))
    app.run_polling()
