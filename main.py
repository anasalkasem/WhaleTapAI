import os
import asyncio
import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.error import TelegramError
import logging

# Apply nest_asyncio for async environments
nest_asyncio.apply()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment variables
TOKEN = os.getenv("BOT_TOKEN")
DOMAIN = os.getenv("WEBHOOK_DOMAIN")
PORT = int(os.getenv("PORT", 8000))

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")
if not DOMAIN:
    raise ValueError("WEBHOOK_DOMAIN environment variable is not set!")
if not DOMAIN.startswith("https://"):
    raise ValueError("DOMAIN must use HTTPS!")

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{DOMAIN}{WEBHOOK_PATH}"

def subscription_buttons():
    """Generate subscription keyboard markup"""
    buttons = [
        [
            InlineKeyboardButton("🧊 FREE Trial", callback_data="subscribe_free"),
            InlineKeyboardButton("⭐ PRO ($20)", callback_data="subscribe_pro")
        ],
        [InlineKeyboardButton("📋 How It Works", callback_data="how_it_works")],
        [InlineKeyboardButton("🏡 Main Menu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(buttons)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /start command"""
    try:
        await update.message.reply_text(
            "👋 Welcome to WhaleTap Bot!\nPlease choose a subscription plan:",
            reply_markup=subscription_buttons()
        )
    except TelegramError as e:
        logger.error(f"Failed to send start message: {e}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors and handle them gracefully"""
    logger.error(f"Update {update} caused error: {context.error}")
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⚠️ An error occurred. Please try again later."
        )
    except Exception as e:
        logger.error(f"Failed to send error message: {e}")

async def main():
    """Start the bot in webhook mode"""
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern="^subscribe_"))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    
    # Add error handler
    application.add_error_handler(error_handler)

    # Set up webhook
    try:
        await application.bot.set_webhook(
            url=WEBHOOK_URL,
            allowed_updates=Update.ALL_TYPES
        )
        logger.info(f"Webhook set to {WEBHOOK_URL}")
    except TelegramError as e:
        logger.error(f"Failed to set webhook: {e}")
        return

    # Start webhook server
    await application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_path=WEBHOOK_PATH,
        allowed_updates=Update.ALL_TYPES
    )

if __name__ == "__main__":
    try:
        logger.info("Starting bot...")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("
