import os
import psycopg2
import nest_asyncio
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# تفعيل nest_asyncio لحل مشكلة event loop
nest_asyncio.apply()

# التوكن ومتغير الاتصال بقاعدة البيانات
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
DATABASE_URL = os.environ.get("DATABASE_URL")

# إعداد اللغات
LANGUAGES = {
    "en": {
        "menu": "Main Menu:",
        "wallet_exists": "Your wallet already exists:\n{wallet}",
        "wallet_created": "New wallet created:\n{wallet}",
        "select_option": "Please choose an option:",
        "buy_success": "Simulated buy order executed successfully ✅",
        "sell_success": "Simulated sell order executed successfully ✅",
        "option_unavailable": "This option is not available yet."
    },
    "ar": {
        "menu": "القائمة الرئيسية:",
        "wallet_exists": "محفظتك موجودة:\n{wallet}",
        "wallet_created": "تم إنشاء محفظة جديدة:\n{wallet}",
        "select_option": "يرجى اختيار خيار:",
        "buy_success": "تم تنفيذ أمر شراء وهمي بنجاح ✅",
        "sell_success": "تم تنفيذ أمر بيع وهمي بنجاح ✅",
        "option_unavailable": "الخيار غير متاح بعد."
    },
    "es": {
        "menu": "Menú principal:",
        "wallet_exists": "Tu billetera ya existe:\n{wallet}",
        "wallet_created": "Nueva billetera creada:\n{wallet}",
        "select_option": "Por favor elige una opción:",
        "buy_success": "Orden de compra simulada ejecutada con éxito ✅",
        "sell_success": "Orden de venta simulada ejecutada con éxito ✅",
        "option_unavailable": "Esta opción no está disponible todavía."
    }
}

user_languages = {}

def get_text(user_id, key):
    lang = user_languages.get(user_id, "en")
    return LANGUAGES.get(lang, LANGUAGES["en"]).get(key, "")

def main_keyboard(user_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Buy | شراء | Comprar", callback_data="buy")],
        [InlineKeyboardButton("Sell | بيع | Vender", callback_data="sell")],
        [InlineKeyboardButton("Auto Trade | تداول تلقائي", callback_data="auto")],
        [InlineKeyboardButton("Stop Copying | إيقاف النسخ | Detener copia", callback_data="stop")],
        [InlineKeyboardButton("Resume Copying | متابعة النسخ | Reanudar copia", callback_data="resume")],
        [InlineKeyboardButton("Set Stop Loss | أمر وقف الخسارة", callback_data="stop_loss")],
        [InlineKeyboardButton("Alerts | تنبيهات | Alertas", callback_data="alerts")],
        [InlineKeyboardButton("My Wallet | محفظتي | Mi billetera", callback_data="wallet")],
        [InlineKeyboardButton("Create Wallet | إنشاء محفظة | Crear billetera", callback_data="create_wallet")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_languages[user_id] = "en"  # Default language
    await update.message.reply_text(
        get_text(user_id, "menu"),
        reply_markup=main_keyboard(user_id)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    try:
        if data == "buy":
            await query.edit_message_text(get_text(user_id, "buy_success"))
            
        elif data == "sell":
            await query.edit_message_text(get_text(user_id, "sell_success"))
            
        elif data == "wallet":
            conn = psycopg2.connect(DATABASE_URL)
            cursor = conn.cursor()
            cursor.execute("SELECT wallet_address FROM whales WHERE user_id = %s;", (user_id,))
            result = cursor.fetchone()
            
            if result:
                await query.edit_message_text(
                    get_text(user_id, "wallet_exists").format(wallet=result[0])
                )
            else:
                await query.edit_message_text(
                    get_text(user_id, "menu"),
                    reply_markup=main_keyboard(user_id)
                )
            cursor.close()
            conn.close()
            
        else:
            await query.edit_message_text(get_text(user_id, "option_unavailable"))
            
    except Exception as e:
        print(f"Error: {e}")
        await query.edit_message_text("An error occurred. Please try again later.")

async def main():
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_handler))
        
        print("Bot is running...")
        await app.run_polling()
        
    except Exception as e:
        print(f"Application error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
