from telegram import Update
from telegram.ext import ContextTypes

# دالة تنفيذ نسخ الصفقة (وهمية حالياً)
async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # رسالة تأكيد وهمية
    await query.edit_message_text(
        text="✅ The latest whale trade has been copied (demo only)."
    )
