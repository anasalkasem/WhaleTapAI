import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from subscriptions.payment_handlers import handle_subscription_choice, handle_payment
from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.keyboards import plans_keyboard
from telegram import Update
from telegram.ext import ContextTypes

# إعداد اللوج
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اختر باقة الاشتراك:",
        reply_markup=plans_keyboard()
    )

# بدء التطبيق باستخدام Webhook
async def main():
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    DOMAIN = os.getenv("WEBHOOK_DOMAIN")  # مثل: https://your-app-name.up.railway.app
    PORT = int(os.environ.get("PORT", 8443))

    application = ApplicationBuilder().token(TOKEN).build()

    # الهاندلرات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern="^subscribe_"))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    # Webhook settings
    await application.initialize()
    await application.bot.set_webhook(f"{DOMAIN}/webhook")
    await application.start()
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="webhook",
        webhook_url=f"{DOMAIN}/webhook"
    )

# التشغيل
if __name__ == "__main__":
    import asyncio
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
