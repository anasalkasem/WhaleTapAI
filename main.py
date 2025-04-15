import os
import psycopg2
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# إعداد الاتصال بقاعدة البيانات
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# إعداد البوت
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# تهيئة سجل الأخطاء
logging.basicConfig(level=logging.INFO)

# الرد على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("شراء", callback_data="buy"), InlineKeyboardButton("بيع", callback_data="sell")],
        [InlineKeyboardButton("نسخ التداول", callback_data="copy"), InlineKeyboardButton("التداول التلقائي", callback_data="auto")],
        [InlineKeyboardButton("إيقاف النسخ", callback_data="stop_copy"), InlineKeyboardButton("متابعة النسخ", callback_data="resume_copy")],
        [InlineKeyboardButton("حد الخسارة", callback_data="stop_loss"), InlineKeyboardButton("تنبيهات", callback_data="alerts")],
        [InlineKeyboardButton("المحفظة", callback_data="wallet"), InlineKeyboardButton("إنشاء محفظة", callback_data="create_wallet")],
        [InlineKeyboardButton("اللغة: عربي", callback_data="lang_ar"), InlineKeyboardButton("Language: English", callback_data="lang_en"), InlineKeyboardButton("Idioma: Español", callback_data="lang_es")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("اختر من القائمة:", reply_markup=reply_markup)

# التعامل مع الضغط على الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "wallet":
        user_id = query.from_user.id
        cursor.execute("SELECT wallet_address FROM whales WHERE id = %s;", (str(user_id),))
        result = cursor.fetchone()
        if result:
            await query.edit_message_text(f"محفظتك موجودة:\n{result[0]}")
        else:
            await query.edit_message_text("لا يوجد محفظة مسجلة.")
    else:
        await query.edit_message_text(f"تم اختيار: {query.data}")

# تهيئة التطبيق
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# تشغيل البوت
if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run_polling())
