import os
import psycopg2
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# تحميل المتغيرات البيئية (اختياري إذا تستخدم ملف .env محلياً)
load_dotenv()

# إعداد التوكن والاتصال بقاعدة البيانات
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

# الاتصال بقاعدة البيانات
def connect_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    # إنشاء الجدول إن لم يكن موجودًا
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS whales (
            id SERIAL PRIMARY KEY,
            wallet_address TEXT UNIQUE,
            activity TEXT
        );
    """)
    conn.commit()
    return conn, cursor

# أمر /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    update.message.reply_text(f"أهلاً {user}! مرحباً بك في بوت WhaleTap لنسخ صفقات الحيتان.")

    # مثال على قراءة المحافظ من قاعدة البيانات
    try:
        conn, cursor = connect_db()
        cursor.execute("SELECT wallet_address, activity FROM whales LIMIT 3;")
        rows = cursor.fetchall()
        if rows:
            msg = "\n".join([f"{row[0]} → {row[1]}" for row in rows])
            update.message.reply_text(f"محافظ نشطة:\n{msg}")
        else:
            update.message.reply_text("لا توجد محافظ مسجلة بعد.")
        cursor.close()
        conn.close()
    except Exception as e:
        update.message.reply_text("حدث خطأ أثناء الاتصال بقاعدة البيانات.")
        print(e)

# إعداد البوت وتشغيله
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
