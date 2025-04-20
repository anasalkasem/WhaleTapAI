from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

# تعريف الحالات للمحادثة
AWAITING_INPUT = {}

# الرد على الضغط على زر إعداد معين
async def handle_auto_trade_setting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    setting_key = query.data.replace("edit_", "")  # استخراج اسم الإعداد من callback_data
    user_id = query.from_user.id

    # حفظ اسم الإعداد المطلوب تغييره
    AWAITING_INPUT[user_id] = setting_key

    await query.edit_message_text(
        text=f"✏️ أدخل القيمة الجديدة لـ: {setting_key.replace('_', ' ')}"
    )

# استقبال القيمة الجديدة من المستخدم
async def receive_setting_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in AWAITING_INPUT:
        await update.message.reply_text("⚠️ لا يوجد إعداد بانتظار التحديث.")
        return

    setting_key = AWAITING_INPUT[user_id]
    new_value = update.message.text.strip()

    # (لاحقًا: احفظ القيمة في قاعدة بيانات)
    await update.message.reply_text(f"✅ تم تحديث {setting_key} إلى: {new_value}")

    # حذف من قائمة الانتظار
    del AWAITING_INPUT[user_id]
