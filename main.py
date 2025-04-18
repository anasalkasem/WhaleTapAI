import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
from subscriptions.main_menu_handler import handle_main_menu  # التصحيح هنا
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

# دالة بدء المحادثة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to WhaleTap!\nPlease use the menu below to start:",
        reply_markup=main_menu_keyboard("en")  # اللغة الافتراضية إنجليزي
    )

async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu))

    # إعداد Webhook
    webhook_url = f"{WEBHOOK_DOMAIN}/webhook"
    logger.info(f"Using Webhook URL: {webhook_url}")
    await application.initialize()
    await application.start()
    await application.bot.set_webhook(webhook_url)
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
