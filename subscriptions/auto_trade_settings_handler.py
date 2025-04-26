from telegram import Update
from telegram.ext import ContextTypes
from models.db_utils import update_user_setting  # نستورد دالة للتحديث في قاعدة البيانات

# تعريف الحالات للمحادثة
AWAITING_INPUT = {}

# الرد على الضغط على زر إعداد معين
async def handle_auto_trade_setting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if not query.data:
        await query.edit_message_text("❌ No setting data found.")
        return

    setting_key = query.data.replace("edit_", "")  # استخراج اسم الإعداد
    user_id = query.from_user.id

    # حفظ اسم الإعداد المطلوب تغييره
    AWAITING_INPUT[user_id] = setting_key

    await query.edit_message_text(
        text=f"✏️ Please enter the new value for {setting_key.replace('_', ' ').title()}:"
    )

# استقبال القيمة الجديدة وتحديثها في قاعدة البيانات
async def receive_setting_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in AWAITING_INPUT:
        await update.message.reply_text("⚠️ No pending setting to update.")
        return

    setting_key = AWAITING_INPUT[user_id]
    new_value = update.message.text.strip()

    # حفظ القيمة في قاعدة البيانات
    success = await update_user_setting(user_id, setting_key, new_value)

    if success:
        await update.message.reply_text(f"✅ Setting '{setting_key}' updated successfully to: {new_value}")
    else:
        await update.message.reply_text(f"❌ Failed to update setting '{setting_key}'.")

    # حذف من قائمة الانتظار
    del AWAITING_INPUT[user_id]
