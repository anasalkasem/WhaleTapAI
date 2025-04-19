from telegram import Update
from telegram.ext import ContextTypes

# زر: 🤖 Auto-Trading
async def handle_auto_trading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="⚙️ تم تفعيل وضع التداول التلقائي.\n"
             "سيتم الآن نسخ صفقات الحيتان تلقائيًا عندما تكون الظروف مناسبة."
    )

# زر: 🛑 Stop Copying
async def handle_stop_copying(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🛑 تم إيقاف نسخ صفقات الحيتان مؤقتًا.\n"
             "يمكنك إعادة التفعيل من القائمة الرئيسية."
    )
from telegram import Update
from telegram.ext import CallbackContext
from subscriptions.auto_trading_keyboard import auto_trading_keyboard

async def handle_auto_trading(update: Update, context: CallbackContext):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="إعدادات التداول التلقائي:",
        reply_markup=auto_trading_keyboard()
    )
