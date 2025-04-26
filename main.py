import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.subscription_handler import handle_main_menu, handle_subscription_info
from subscriptions.settings_handler import handle_settings
from subscriptions.auto_trading_handlers import handle_auto_trading
from subscriptions.copy_trade_handler import handle_copy_trade
from subscriptions.insights_handler import handle_smart_insights
from subscriptions.stop_copying_handler import handle_stop_copying
from subscriptions.stats_handler import handle_my_stats
from subscriptions.free_plan_handler import handle_free_plan
from admin.confirm_payment_handler import handle_confirm_payment
from models.init_db import init_db
from subscriptions.trading_menu_handler import handle_trading_menu

# Initialize the database
init_db()

TOKEN = os.getenv("BOT_TOKEN")
application = Application.builder().token(TOKEN).build()

# Command Handlers
application.add_handler(CommandHandler("start", handle_main_menu))

# CallbackQuery Handlers
application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
application.add_handler(CallbackQueryHandler(handle_auto_trading, pattern="^auto_trading$"))
application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))
application.add_handler(CallbackQueryHandler(handle_smart_insights, pattern="^smart_insights$"))
application.add_handler(CallbackQueryHandler(handle_stop_copying, pattern="^stop_copying$"))
application.add_handler(CallbackQueryHandler(handle_my_stats, pattern="^my_stats$"))
application.add_handler(CallbackQueryHandler(handle_free_plan, pattern="^subscribe_free$"))
application.add_handler(CallbackQueryHandler(handle_confirm_payment, pattern="^admin_confirm_payment$"))
application.add_handler(CallbackQueryHandler(handle_trading_menu, pattern="^trading$"))

if __name__ == "__main__":
    application.run_polling()
