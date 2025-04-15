import os
import psycopg2
from psycopg2 import sql, errors
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد الاتصال بقاعدة البيانات
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# إنشاء جدول المحافظ إذا لم يكن موجودًا
cursor.execute("""
    CREATE TABLE IF NOT EXISTS whales (
        id SERIAL PRIMARY KEY,
        wallet_address TEXT UNIQUE,
        activity TEXT
    );
""")
conn.commit()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في WhaleTap! أرسل /addwallet <محفظتك> لإضافتها.")

# أمر /addwallet
async def add_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("الرجاء إرسال عنوان المحفظة بعد الأمر مثل:\n/addwallet So1anaWhaleWallet")
        return

    wallet = context.args[0]
    try:
        cursor.execute("INSERT INTO whales (wallet_address, activity) VALUES (%s, %s)", (wallet, 'unknown'))
        conn.commit()
        await update.message.reply_text(f"تمت إضافة المحفظة: {wallet}")
    except errors.UniqueViolation:
        conn.rollback()
        await update.message.reply_text("هذه المحفظة مضافة مسبقًا.")
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {str(e)}")

# تشغيل البوت
async def main():
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("addwallet", add_wallet))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
