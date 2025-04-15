import os
import psycopg2
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد الاتصال بقاعدة البيانات
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# إنشاء جدول إذا لم يكن موجود
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
    await update.message.reply_text("أهلاً بك في بوت WhaleTap!")

# تشغيل التطبيق
async def main():
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    await app.initialize()
    await app.start()
    print("Bot is running...")
    await app.updater.start_polling()
    await app.updater.idle()

# الحل لمشكلة event loop
import asyncio

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()