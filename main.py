import os
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

from subscriptions.subscription_plans import PLANS
from subscriptions.payment_handlers import handle_subscription_choice, handle_payment
from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.subscription_buttons import subscription_buttons

nest_asyncio.apply()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN is not set!")
if not WEBHOOK_DOMAIN:
    raise Exception("WEBHOOK_DOMAIN is not set!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اختر باقة الاشتراك:",
        reply_markup=subscription_buttons()
    )

def main_menu_callback_filter(data: str) -> bool:
    return data == "main_menu"

def subscription_callback_filter(data: str) -> bool:
    return data in ["subscribe_pro", "subscribe_free"]

def payment_callback_filter(data: str) -> bool:
    return data.startswith("pay_")

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern=main_menu_callback_filter))
    application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern=subscription_callback_filter))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern=payment_callback_filter))

    # Webhook
    DOMAIN = f"https://{WEBHOOK_DOMAIN}" if not WEBHOOK_DOMAIN.startswith("http") else WEBHOOK_DOMAIN
    print("DOMAIN =", DOMAIN)

    await application.bot.set_webhook(f"{DOMAIN}/webhook")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
