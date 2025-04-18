import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from whale_ui.main_menu_handler import handle_main_menu
from subscriptions.trade_handlers import handle_copy_trade

# إعداد اللوج
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")
WEBHOOK_PATH = f"/{BOT_TOKEN}"

if not BOT_TOKEN or not WEBHOOK_DOMAIN:
    raise ValueError("يجب تعيين TELEGRAM_BOT_TOKEN و WEBHOOK_DOMAIN في متغيرات البيئة")

WEBHOOK_URL = f"{WEBHOOK_DOMAIN}{WEBHOOK_PATH}"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📥 Copy Latest Trade", callback_data="copy_trade"),
            InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")
        ],
        [
            InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
            InlineKeyboardButton("📊 My Portfolio", callback_data="portfolio")
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("🧠 Smart Whale Insights", callback_data="insights")
        ],
        [
            InlineKeyboardButton("💳 Upgrade to PRO", callback_data="subscribe_pro"),
            InlineKeyboardButton("🆓 Free Plan", callback_data="subscribe_free")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to WhaleTap AI.\nChoose an option below:", reply_markup=reply_markup)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Webhook settings
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8443)),
        webhook_url=WEBHOOK_URL,
        path=WEBHOOK_PATH
    )

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu))
    application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))

    logger.info("Starting bot with Webhook...")

if __name__ == "__main__":
    main()
