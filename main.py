import os
from telegram.ext import Application, CommandHandler
from models.init_db import init_db
from handlers_register import add_handlers  # <-- إضافة كل الهاندلرات هنا

# تهيئة قاعدة البيانات
init_db()

# جلب التوكن من المتغيرات البيئية
TOKEN = os.getenv("BOT_TOKEN")
application = Application.builder().token(TOKEN).build()

# تعريف أمر /start
async def handle_start(update, context):
    from subscriptions.subscription_handler import handle_main_menu
    await handle_main_menu(update, context)

application.add_handler(CommandHandler("start", handle_start))

# إضافة جميع الهاندلرز
add_handlers(application)

if __name__ == "__main__":
    application.run_polling()
