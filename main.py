import asyncio
import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram import Update
from telegram.ext import ContextTypes
import nest_asyncio

from subscriptions.subscription_plans import handle_subscription_buttons
from subscriptions.payment_handlers import handle_subscription_selection
from subscriptions.main_menu_handler import handle_main_menu

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")

if not TOKEN:
    raise Exception("BOT_TOKEN is not set!")
if not WEBHOOK_DOMAIN:
    raise Exception("WEBHOOK_DOMAIN is not set!")

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_DOMAIN.rstrip('/')}{WEBHOOK_PATH}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اختر باقة الاشتراك:",
        reply_markup=await handle_subscription_buttons()
    )

async def main():
    application = Application.builder().token(TOKEN).build()

    # هنا يتم ربط الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_subscription_selection, pattern="^subscribe_"))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    # تهيئة البوت للعمل مع Webhook
    await application.initialize()
    await application.bot.set_webhook(WEBHOOK_URL)
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(main())
