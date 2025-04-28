import os
from telegram.ext import Application, CommandHandler
from models.init_db import init_db
from subscriptions.subscription_handler import add_handlers, handle_main_menu

# تهيئة قاعدة البيانات
init_db()

# جلب توكن البوت
TOKEN = os.getenv("BOT_TOKEN")
application = Application.builder().token(TOKEN).build()

# تعريف دالة /start
async def handle_start(update, context):
    await handle_main_menu(update, context)

# إضافة هندلر أمر /start
application.add_handler(CommandHandler("start", handle_start))

# إضافة جميع الهاندلرات الأخرى
add_handlers(application)

if __name__ == "__main__":
    application.run_polling()
