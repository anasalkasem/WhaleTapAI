import os
import logging
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.copy_trade_handler import handle_copy_trade

# إعداد اللوجر
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# إعداد المتغيرات
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")  # مثل: https://your-domain.railway.app

if not TOKEN:
    raise ValueError("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")

if not WEBHOOK_DOMAIN:
    raise ValueError("لم يتم تعيين WEBHOOK_DOMAIN في متغيرات البيئة")

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_DOMAIN}{WEBHOOK_PATH}"

# دالة بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_main_menu(update, context)

# دالة التشغيل الرئيسية
async def main():
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))

    logger.info(f"Using Webhook URL: {WEBHOOK_URL}")
    await application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8443)),
        webhook_path=WEBHOOK_PATH,
        url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
