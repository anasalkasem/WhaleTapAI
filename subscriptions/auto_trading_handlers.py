from telegram import Update
from telegram.ext import ContextTypes

# تفعيل التداول التلقائي (وهمي حالياً)
async def handle_auto_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text="🤖 Auto-Trading has been enabled (demo mode)."
    )

# إيقاف نسخ التداول (وهمي حالياً)
async def handle_stop_copying(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text="🛑 Copying trades has been stopped (demo mode)."
    )
