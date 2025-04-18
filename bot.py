import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.main_menu_handler import (
    handle_main_menu,
    handle_subscription_info,
    handle_back_to_plans,
)

TOKEN = os.getenv("BOT_TOKEN")

def main():
    application = Application.builder().token(TOKEN).build()

    # أوامر البوت
    application.add_handler(CommandHandler("start", handle_main_menu))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
    application.add_handler(CallbackQueryHandler(handle_back_to_plans, pattern="^back_to_plans$"))

    # تشغيل البوت
    application.run_polling()

if __name__ == "__main__":
    main()