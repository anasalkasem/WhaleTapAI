import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from subscriptions.main_menu_handler import handle_main_menu

# إعداد اللوجر
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# التوكن من متغير البيئة الصحيح
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")

# دالة بدء المحادثة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_main_menu(update, context)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu))

    logger.info("Bot started successfully.")
    application.run_polling()

if __name__ == "__main__":
    main()
