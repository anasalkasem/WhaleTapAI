import asyncio
import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
)
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from subscriptions.payment_handlers import (
    handle_subscription_choice,
    handle_payment
)
from subscriptions.keyboards import plans_keyboard
from subscriptions.main_menu_handler import handle_main_menu

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

# بدء التطبيق
async def main():
    import nest_asyncio
    nest_asyncio.apply()

    from dotenv import load_dotenv
    import os
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")

    application = ApplicationBuilder().token(TOKEN).build()

    # الهاندلرات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern="^subscribe_"))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    # التشغيل
    await application.run_polling()

# تشغيل البوت
if __name__ == "__main__":
    asyncio.run(main())
