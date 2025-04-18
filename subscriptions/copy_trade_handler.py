from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard
from models.database import Session  # تعديل الاستيراد الصحيح

# دالة تنفيذ نسخ صفقة الحوت
async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    lang = context.user_data.get("lang", "ar")

    # إنشاء جلسة قاعدة البيانات
    session = Session()

    # (هنا ممكن لاحقاً تضيف كود حفظ صفقة في قاعدة البيانات)

    # رسالة التأكيد
    if lang == "en":
        text = "✅ The whale trade has been copied successfully!"
    elif lang == "es":
        text = "✅ ¡La operación de la ballena se ha copiado con éxito!"
    else:
        text = "✅ تم نسخ صفقة الحوت بنجاح!"

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=main_menu_keyboard(lang)
    )
