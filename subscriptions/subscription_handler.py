from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from subscriptions.keyboards import main_menu_keyboard
from admin.confirm_payment_handler import handle_confirm_payment  # <-- إضافة مهمة

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        user_id = query.from_user.id
        keyboard = main_menu_keyboard(user_id)
        await query.answer()
        await query.edit_message_text(
            text="🏠 Main Menu:",
            reply_markup=keyboard
        )
    else:
        user_id = update.effective_user.id
        keyboard = main_menu_keyboard(user_id)
        await update.message.reply_text(
            text="🏠 Main Menu:",
            reply_markup=keyboard
        )

async def handle_subscription_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        user_id = query.from_user.id
        keyboard = main_menu_keyboard(user_id)
        await query.answer()
        await query.edit_message_text(
            text="💳 Choose your plan and unlock premium features!",
            reply_markup=keyboard
        )
    else:
        user_id = update.effective_user.id
        keyboard = main_menu_keyboard(user_id)
        await update.message.reply_text(
            text="💳 Choose your plan and unlock premium features!",
            reply_markup=keyboard
        )

# إضافة هندلر زر الادمن "Confirm Payment"
def add_handlers(application):
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
    application.add_handler(CallbackQueryHandler(handle_confirm_payment, pattern="^admin_confirm_payment$"))  # زر الأدمن
