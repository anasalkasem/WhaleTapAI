import os
from telegram.ext import Application, CommandHandler
from subscriptions.handlers_register import add_handlers
from models.init_db import init_db

# تهيئة قاعدة البيانات
init_db()

# جلب توكن البوت
TOKEN = os.getenv("BOT_TOKEN")
application = Application.builder().token(TOKEN).build()

# دالة أمر /start
async def handle_start(update, context):
    from subscriptions.subscription_handler import handle_main_menu
    await handle_main_menu(update, context)

# إضافة هندلر /start
application.add_handler(CommandHandler("start", handle_start))

# إضافة كل الهاندلرات من ملف handlers_register.py
add_handlers(application)

# تشغيل البوت
if __name__ == "__main__":
    application.run_polling()
