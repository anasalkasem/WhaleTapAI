import os
import logging
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.copy_trade_handler import handle_copy_trade
from subscriptions.auto_trading_handlers import handle_auto_trading, handle_stop_copying

# إعداد اللوجر
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# تحميل التوكن والدومين من البيئة
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")

if not TOKEN:
    raise ValueError("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")

if not WEBHOOK_DOMAIN:
    raise ValueError("لم يتم تعيين WEBHOOK_DOMAIN في متغيرات البيئة")

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_DOMAIN}{WEBHOOK_PATH}"

# دالة بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_main_menu(update, context)

# الدالة الرئيسية لتشغيل البوت
async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))
    application.add_handler(CallbackQueryHandler(handle_auto_trading, pattern="^auto_trading$"))
    application.add_handler(CallbackQueryHandler(handle_stop_copying, pattern="^stop_copying$"))

    logger.info(f"Using Webhook URL: {WEBHOOK_URL}")
    await application.initialize()
    await application.start()
    await application.bot.set_webhook(url=WEBHOOK_URL)

# تشغيل البوت
if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
