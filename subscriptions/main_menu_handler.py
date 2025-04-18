from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import main_menu_keyboard, plans_keyboard

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = main_menu_keyboard()
    text = "🚀 Welcome to WhaleTap!\nChoose an option below to get started."

    if update.message:
        await update.message.reply_text(text, reply_markup=keyboard)
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

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
