import asyncio
import logging
import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# تحميل متغيرات البيئة
load_dotenv()

from subscriptions.payment_handlers import handle_subscription_choice, handle_payment
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
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    # الهاندلرات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern="^subscribe_"))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    await application.run_polling()

# تنفيذ البوت
if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
