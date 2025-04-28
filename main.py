import os
from telegram.ext import Application, CommandHandler

# استيراد وظيفة إضافة كل الهاندلرات دفعة وحدة
from subscriptions.subscription_handler import add_handlers
from models.init_db import init_db

# تهيئة قاعدة البيانات
init_db()

# جلب توكن البوت
TOKEN = os.getenv("BOT_TOKEN")
application = Application.builder().token(TOKEN).build()

# أمر /start يفتح القائمة الرئيسية
application.add_handler(CommandHandler("start", handle_start))

# تعريف دالة /start
async def handle_start(update, context):
    from subscriptions.subscription_handler import handle_main_menu
    await handle_main_menu(update, context)

# إضافة جميع الهاندلرز دفعة وحدة
add_handlers(application)

if __name__ == "__main__":
    application.run_polling()
