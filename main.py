import asyncio
import logging
import os
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
)
from telegram import Update
from telegram.ext import ContextTypes

from subscriptions.payment_handlers import (
    handle_subscription_choice,
    handle_payment
)
from subscriptions.main_menu_handler import handle_main_menu
from subscriptions.keyboards import plans_keyboard

# إعدادات اللوج
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

# بدء التطبيق
async def main():
    TOKEN = os.getenv("BOT_TOKEN")
    DOMAIN = os.getenv("WEBHOOK_DOMAIN")  # تأكد من إضافته في Railway

    print("DOMAIN =", DOMAIN)  # للتأكد من القيمة
    if not DOMAIN:
        raise Exception("WEBHOOK_DOMAIN is not set!")

    application = ApplicationBuilder().token(TOKEN).build()

    # الهاندلرات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern="^subscribe_"))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    # إعداد Webhook
    await application.bot.set_webhook(f"{DOMAIN}/webhook")
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

# تنفيذ البوت
if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
