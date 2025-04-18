from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import main_menu_keyboard, plans_keyboard

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")  # اللغة الافتراضية: عربي

    if lang == "en":
        text = "🚀 <b>Welcome to WhaleTap!</b>\nChoose an option below to get started."
    elif lang == "es":
        text = "🚀 <b>¡Bienvenido a WhaleTap!</b>\nElige una opción para comenzar."
    else:
        text = "🚀 <b>مرحباً بك في WhaleTap!</b>\nاختر خياراً للبدء."

    keyboard = main_menu_keyboard()

    if update.message:
        await update.message.reply_text(text, reply_markup=keyboard, parse_mode="HTML")
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")
async def handle_subscription_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="💳 اختر نوع الاشتراك المناسب لك:",
        reply_markup=plans_keyboard()
    )

async def handle_back_to_plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="💳 الرجوع لاختيار نوع الاشتراك:",
        reply_markup=plans_keyboard()
    )
    
# --- ردود تفاعلية إضافية ---

async def handle_subscription_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="💳 اختر نوع الاشتراك المناسب لك:",
        reply_markup=plans_keyboard()
    )

async def handle_back_to_plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="💳 الرجوع لاختيار نوع الاشتراك:",
        reply_markup=plans_keyboard()
    )
