import os
import psycopg2
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# الاتصال بقاعدة البيانات
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# إنشاء الجداول المطلوبة
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_wallets (
    id SERIAL PRIMARY KEY,
    user_id BIGINT UNIQUE,
    wallet_address TEXT
);
CREATE TABLE IF NOT EXISTS user_settings (
    id SERIAL PRIMARY KEY,
    user_id BIGINT UNIQUE,
    language TEXT DEFAULT 'ar',
    notifications_enabled BOOLEAN DEFAULT TRUE,
    copy_trading_enabled BOOLEAN DEFAULT FALSE,
    stop_loss_enabled BOOLEAN DEFAULT FALSE
);
CREATE TABLE IF NOT EXISTS trades (
    id SERIAL PRIMARY KEY,
    user_id BIGINT,
    action TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()

# عرض لوحة الأزرار
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("شراء | Buy | Comprar", callback_data='buy'),
         InlineKeyboardButton("بيع | Sell | Vender", callback_data='sell')],
        [InlineKeyboardButton("نسخ التداول | Copy Trade | Copiar Trade", callback_data='copy_trade'),
         InlineKeyboardButton("إيقاف النسخ | Stop Copy | Detener Copia", callback_data='stop_copy')],
        [InlineKeyboardButton("متابعة النسخ | Resume Copy | Reanudar Copia", callback_data='resume_copy'),
         InlineKeyboardButton("أوامر الحد | Stop-Loss | Stop-Loss", callback_data='stop_loss')],
        [InlineKeyboardButton("محفظتي | My Wallet | Mi Billetera", callback_data='my_wallet'),
         InlineKeyboardButton("إنشاء محفظة | Create Wallet | Crear Billetera", callback_data='create_wallet')],
        [InlineKeyboardButton("الإشعارات | Notifications | Notificaciones", callback_data='notifications'),
         InlineKeyboardButton("الإعدادات | Settings | Configuración", callback_data='settings')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("اختر خياراً من القائمة:", reply_markup=reply_markup)

# التعامل مع الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    action = query.data

    cursor = conn.cursor()

    if action == "create_wallet":
        cursor.execute("SELECT wallet_address FROM user_wallets WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            await query.edit_message_text(f"محفظتك موجودة:\n{result[0]}")
{result[0]}")
        else:
            wallet = f"Wallet_{user_id}_SOL"
            cursor.execute("INSERT INTO user_wallets (user_id, wallet_address) VALUES (%s, %s)", (user_id, wallet))
            conn.commit()
            await query.edit_message_text(f"تم إنشاء محفظة جديدة:
{wallet}")

    elif action == "my_wallet":
        cursor.execute("SELECT wallet_address FROM user_wallets WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            await query.edit_message_text(f"محفظتك:
{result[0]}")
        else:
            await query.edit_message_text("لا توجد محفظة مرتبطة بحسابك.")

    elif action in ["buy", "sell"]:
        cursor.execute("INSERT INTO trades (user_id, action) VALUES (%s, %s)", (user_id, action))
        conn.commit()
        await query.edit_message_text(f"تم تسجيل عملية: {action}")

    elif action == "copy_trade":
        cursor.execute("UPDATE user_settings SET copy_trading_enabled = TRUE WHERE user_id = %s RETURNING user_id", (user_id,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO user_settings (user_id, copy_trading_enabled) VALUES (%s, TRUE)", (user_id,))
        conn.commit()
        await query.edit_message_text("تم تفعيل نسخ التداول.")

    elif action == "stop_copy":
        cursor.execute("UPDATE user_settings SET copy_trading_enabled = FALSE WHERE user_id = %s", (user_id,))
        conn.commit()
        await query.edit_message_text("تم إيقاف نسخ التداول.")

    elif action == "resume_copy":
        cursor.execute("UPDATE user_settings SET copy_trading_enabled = TRUE WHERE user_id = %s", (user_id,))
        conn.commit()
        await query.edit_message_text("تمت متابعة نسخ التداول.")

    elif action == "stop_loss":
        cursor.execute("UPDATE user_settings SET stop_loss_enabled = NOT stop_loss_enabled WHERE user_id = %s RETURNING stop_loss_enabled", (user_id,))
        new_status = cursor.fetchone()[0]
        conn.commit()
        txt = "تم تفعيل أمر الحد من الخسارة." if new_status else "تم إلغاء أمر الحد من الخسارة."
        await query.edit_message_text(txt)

    elif action == "notifications":
        cursor.execute("UPDATE user_settings SET notifications_enabled = NOT notifications_enabled WHERE user_id = %s RETURNING notifications_enabled", (user_id,))
        new_status = cursor.fetchone()[0]
        conn.commit()
        txt = "تم تفعيل الإشعارات." if new_status else "تم إيقاف الإشعارات."
        await query.edit_message_text(txt)

    elif action == "settings":
        await query.edit_message_text("سيتم قريباً دعم تغيير اللغة والتخصيص.")

# إعداد البوت
async def main():
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    await app.initialize()
    await app.start()
    print("WhaleTap Bot is running...")
    await app.updater.start_polling()
    await app.updater.idle()

# حل مشكلة event loop
import asyncio
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()