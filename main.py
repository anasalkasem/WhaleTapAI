import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from subscriptions.main_menu_handler import handle_main_menu

# إعداد اللوج
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# قراءة التوكن من متغيرات البيئة
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")

# أمر /start يعرض زر القائمة الرئيسية فقط
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        {"text": "📋 Main Menu", "callback_data": "main_menu"}
    ]]
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📋 Main Menu", callback_data="main_menu")]
    ])
    await update.message.reply_text("مرحباً بك في WhaleTap Bot!\nاختر من القائمة:", reply_markup=reply_markup)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    app.run_polling()

if __name__ == "__main__":
    main()
