import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.keyboards import main_menu_keyboard

# إعداد اللوجر
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# متغيرات البيئة
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")

if not BOT_TOKEN:
    raise ValueError("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")
if not WEBHOOK_DOMAIN:
    raise ValueError("لم يتم تعيين WEBHOOK_DOMAIN في متغيرات البيئة")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to WhaleTap!\nPlease use the menu below to start:",
        reply_markup=main_menu_keyboard("en")
    )

# Main
async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu))

    # Webhook
    webhook_url = f"{WEBHOOK_DOMAIN}/webhook"
    logger.info(f"Using Webhook URL: {webhook_url}")

    await application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        webhook_url=webhook_url,
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
