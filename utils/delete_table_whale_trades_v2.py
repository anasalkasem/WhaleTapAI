from telegram import Update
from telegram.ext import ContextTypes
from models.database import Session, WhaleTrade

# معرف الأدمن
ADMIN_ID = 6672291052

# دالة حذف سجل الصفقات
async def handle_delete_trades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = context.user_data.get("lang", "ar")

    # التحقق إذا المستخدم أدمن
    if user_id != ADMIN_ID:
        if lang == "en":
            text = "⚠️ You are not authorized to perform this action."
        elif lang == "es":
            text = "⚠️ No estás autorizado para realizar esta acción."
        else:
            text = "⚠️ ليس لديك صلاحية تنفيذ هذا الإجراء."
    else:
        # حذف كل الصفقات من قاعدة البيانات
        session = Session()
        session.query(WhaleTrade).delete()
        session.commit()
        session.close()

        if lang == "en":
            text = "✅ All whale trades have been deleted successfully."
        elif lang == "es":
            text = "✅ Todas las operaciones han sido eliminadas correctamente."
        else:
            text = "✅ تم حذف جميع صفقات الحيتان بنجاح."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)
