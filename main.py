from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.main_menu_handler import (
    handle_main_menu,
    handle_subscription_info,
    handle_back_to_plans,
)
from telegram import Update
from telegram.ext import ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

application = Application.builder().token(TOKEN).build()

# أوامر البداية
application.add_handler(CommandHandler("start", handle_main_menu))

# الكولباك من الأزرار
application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
application.add_handler(CallbackQueryHandler(handle_back_to_plans, pattern="^back_to_plans$"))

if __name__ == "__main__":
    application.run_polling()
