import logging
import os
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ContextTypes
)
from subscriptions.main_menu import main_menu_keyboard
from subscriptions.main_menu_handler import handle_main_menu

# إعداد اللوجر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# الحصول على التوكن من متغيرات البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is missing!")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome! Please select an option:",
        reply_markup=main_menu_keyboard()
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # الأوامر والمعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
