import os
import psycopg2
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

LANGUAGES = {
    "ar": {
        "welcome": "أهلًا بك في بوت WhaleTap!",
        "menu": "اختر من القائمة:",
        "buy": "شراء",
        "sell": "بيع",
        "copy": "نسخ التداول",
        "auto": "التداول التلقائي",
        "stop": "إيقاف النسخ",
        "resume": "متابعة النسخ",
        "loss": "حد الخسارة",
        "alerts": "تنبيهات",
        "wallet": "المحفظة",
        "create_wallet": "إنشاء محفظة",
        "lang": "اللغة: عربي"
    },
    "en": {
        "welcome": "Welcome to WhaleTap Bot!",
        "menu": "Choose from the menu:",
        "buy": "Buy",
        "sell": "Sell",
        "copy": "Copy Trading",
        "auto": "Auto Trading",
        "stop": "Stop Copy",
        "resume": "Resume Copy",
        "loss": "Stop Loss",
        "alerts": "Alerts",
        "wallet": "Wallet",
        "create_wallet": "Create Wallet",
        "lang": "Language: English"
    },
    "es": {
        "welcome": "¡Bienvenido al bot WhaleTap!",
        "menu": "Elige del menú:",
        "buy": "Comprar",
        "sell": "Vender",
        "copy": "Copiar operaciones",
        "auto": "Auto trading",
        "stop": "Detener copia",
        "resume": "Reanudar copia",
        "loss": "Límite de pérdida",
        "alerts": "Alertas",
        "wallet": "Cartera",
        "create_wallet": "Crear cartera",
        "lang": "Idioma: Español"
    }
}

user_lang = {}

def get_text(user_id, key):
    lang = user_lang.get(user_id, "ar")
    return LANGUAGES[lang][key]

def main_keyboard(user_id):
    lang = user_lang.get(user_id, "ar")
    texts = LANGUAGES[lang]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(texts["buy"], callback_data="buy"),
         InlineKeyboardButton(texts["sell"], callback_data="sell")],
        [InlineKeyboardButton(texts["copy"], callback_data="copy"),
         InlineKeyboardButton(texts["auto"], callback_data="auto")],
        [InlineKeyboardButton(texts["stop"], callback_data="stop"),
         InlineKeyboardButton(texts["resume"], callback_data="resume")],
        [InlineKeyboardButton(texts["loss"], callback_data="loss"),
         InlineKeyboardButton(texts["alerts"], callback_data="alerts")],
        [InlineKeyboardButton(texts["wallet"], callback_data="wallet"),
         InlineKeyboardButton(texts["create_wallet"], callback_data="create_wallet")],
        [InlineKeyboardButton("اللغة: عربي", callback_data="lang_ar"),
         InlineKeyboardButton("Language: English", callback_data="lang_en"),
         InlineKeyboardButton("Idioma: Español", callback_data="lang_es")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_lang[user_id] = "ar"
    await update.message.reply_text(
        get_text(user_id, "welcome"),
        reply_markup=main_keyboard(user_id)
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    data = query.data

    if data.startswith("lang_"):
        user_lang[user_id] = data.split("_")[1]
        await query.edit_message_text(get_text(user_id, "menu"), reply_markup=main_keyboard(user_id))
    else:
await query.edit_message_text(f"{get_text(user_id, 'menu')}", reply_markup=main_keyboard(user_id))

تم اختيار: {data}")

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_callback))

if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run_polling())
