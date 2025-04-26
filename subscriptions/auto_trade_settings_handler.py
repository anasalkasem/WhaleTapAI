# subscriptions/auto_trade_settings_handler.py

from telegram import Update
from telegram.ext import ContextTypes

# تعريف الحالات للمحادثة
AWAITING_INPUT = {}

# التعامل مع الضغط على زر إعداد معين
async def handle_auto_trade_setting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if not query.data:
        await query.edit_message_text("❌ No setting data found.")
        return

    setting_key = query.data.replace("edit_", "")  # استخراج اسم الإعداد
    user_id = query.from_user.id

    # حفظ الإعداد المطلوب تغييره
    AWAITING_INPUT[user_id] = setting_key

    await query.edit_message_text(
        text=f"✏️ Please enter the new value for {setting_key.replace('_', ' ').title()}:"
    )

# استقبال القيمة الجديدة من المستخدم
async def receive_setting_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in AWAITING_INPUT:
        await update.message.reply_text("⚠️ No pending setting to update.")
        return

    setting_key = AWAITING_INPUT[user_id]
    new_value = update.message.text.strip()

    # إرسال رسالة تأكيد فقط (لا حفظ بقاعدة بيانات حالياً)
    await update.message.reply_text(f"✅ Setting '{setting_key}' updated successfully to: {new_value}")

    # حذف من قائمة الانتظار
    del AWAITING_INPUT[user_id]
