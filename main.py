import os
import asyncio
import nest_asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.payment_handlers import handle_payment, handle_subscription_choice
from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.subscription_plans import PLANS
from telegram import Update
from telegram.ext import ContextTypes

nest_asyncio.apply()

TOKEN = os.getenv("BOT_TOKEN")
DOMAIN = os.getenv("WEBHOOK_DOMAIN")

if not TOKEN:
    raise Exception("BOT_TOKEN is not set!")

if not DOMAIN:
    raise Exception("WEBHOOK_DOMAIN is not set!")

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{DOMAIN}{WEBHOOK_PATH}"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحباً بك في بوت WhaleTap.\nيرجى اختيار باقة الاشتراك:",
        reply_markup=subscription_buttons()
    )


def subscription_buttons():
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup

    buttons = [
        [
            InlineKeyboardButton("نسخة تجريبية 🧊 FREE", callback_data="subscribe_free"),
            InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro")
        ],
        [InlineKeyboardButton("📋 كيف يعمل البوت؟", callback_data="how_it_works")],
        [InlineKeyboardButton("🏡 القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(buttons)


async def main():
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern="^subscribe_"))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))

    # Webhook config
    await application.bot.set_webhook(url=WEBHOOK_URL)
    print(f"DOMAIN = {DOMAIN}")
    await application.initialize()
    await application.start()
    await application.run_polling()  # أو استخدم await application.run_webhook(...) لو أردت webhook فقط


if __name__ == "__main__":
    asyncio.run(main())
