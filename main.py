
import os
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.main_menu import main_menu_keyboard

# إعداد اللوجر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# قراءة التوكن والدومين من متغيرات البيئة
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")

if not BOT_TOKEN:
    raise ValueError("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")
if not WEBHOOK_DOMAIN:
    raise ValueError("لم يتم تعيين WEBHOOK_DOMAIN في متغيرات البيئة")

# دالة البداية
async def start(update, context):
    await update.message.reply_text(
        "🚀 Welcome to WhaleTap!",
        reply_markup=main_menu_keyboard()
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # الأوامر والمعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu))

    logger.info("Starting bot with Webhook...")
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get('PORT', 8443)),
        webhook_url=f"{WEBHOOK_DOMAIN}/webhook"
    )

if __name__ == "__main__":
    main()
