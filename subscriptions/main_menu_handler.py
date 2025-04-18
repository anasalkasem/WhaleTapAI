from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import main_menu_keyboard, plans_keyboard

# القائمة الرئيسية
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

# الاشتراك
async def handle_subscription_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")

    if lang == "en":
        text = "💳 Choose your subscription plan:"
    elif lang == "es":
        text = "💳 Elige tu plan de suscripción:"
    else:
        text = "💳 اختر نوع الاشتراك المناسب لك:"

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=plans_keyboard()
    )

# الرجوع إلى خطط الاشتراك
async def handle_back_to_plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")

    if lang == "en":
        text = "💳 Back to subscription plans:"
    elif lang == "es":
        text = "💳 Volver a los planes de suscripción:"
    else:
        text = "💳 الرجوع لاختيار نوع الاشتراك:"

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=plans_keyboard()
    )
lang = context.user_data.get("lang", "ar")
keyboard = main_menu_keyboard(lang)
