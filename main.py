# main.py

import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# باقي الهاندلرات
from subscriptions.subscription_handler import handle_main_menu
from subscriptions.settings_handler import handle_settings
from subscriptions.auto_trade_settings_handler import handle_auto_trade_setting, receive_setting_input
from subscriptions.copy_trade_handler import handle_copy_trade
from subscriptions.insights_handler import handle_smart_insights
from subscriptions.stop_copying_handler import handle_stop_copying
from subscriptions.stats_handler import handle_my_stats
from subscriptions.free_plan_handler import handle_free_plan
from admin.confirm_payment_handler import handle_confirm_payment
from subscriptions.trading_menu_handler import handle_trading_menu

# استيراد وظيفة الاشتراك المدفوع الجديدة
from utils.confirm_payment import handle_subscribe_pro

from models.init_db import init_db

# Initialize the database
init_db()

TOKEN = os.getenv("BOT_TOKEN")
application = Application.builder().token(TOKEN).build()

# Command Handlers
application.add_handler(CommandHandler("start", handle_main_menu))

# CallbackQuery Handlers
application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
application.add_handler(CallbackQueryHandler(handle_auto_trade_setting, pattern="^auto_trading$"))
application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))
application.add_handler(CallbackQueryHandler(handle_smart_insights, pattern="^smart_insights$"))
application.add_handler(CallbackQueryHandler(handle_stop_copying, pattern="^stop_copying$"))
application.add_handler(CallbackQueryHandler(handle_my_stats, pattern="^my_stats$"))
application.add_handler(CallbackQueryHandler(handle_free_plan, pattern="^subscribe_free$"))
application.add_handler(CallbackQueryHandler(handle_confirm_payment, pattern="^admin_confirm_payment$"))
application.add_handler(CallbackQueryHandler(handle_trading_menu, pattern="^trading$"))
application.add_handler(CallbackQueryHandler(handle_subscribe_pro, pattern="^subscribe_pro$"))

if __name__ == "__main__":
    application.run_polling()
