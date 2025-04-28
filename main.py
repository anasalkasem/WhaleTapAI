import os
from telegram.ext import Application, CommandHandler
from subscriptions.handlers_register import add_handlers  # استدعاء جميع الهاندلرز من ملف واحد
from models.init_db import init

ممتاز!  
جاهز لك الآن نسخة احترافية من `main.py` تتناسب مع شغلك الجديد بدون لخبطه:

---

### نسخة `main.py` الجديدة:

```python
import os
from telegram.ext import Application, CommandHandler
from subscriptions.handlers_register import add_handlers  # استيراد الهاندلرات المجمعة
from models.init_db import init_db
from subscriptions.subscription_handler import handle_main_menu  # أمر /start يستخدم نفس القائمة الرئيسية

# تهيئة قاعدة البيانات
init_db()

# جلب توكن البوت
TOKEN = os.getenv("BOT_TOKEN")

# تهيئة التطبيق
application = Application.builder().token(TOKEN).build()

# أمر /start
async def handle_start(update, context):
    await handle_main_menu(update, context)

# إضافة أمر /start
application.add_handler(CommandHandler("start", handle_start))

# إضافة كل أزرار البوت (الهاندلرات)
add_handlers(application)

# تشغيل البوت
if __name__ == "__main__":
    application.run_polling()
