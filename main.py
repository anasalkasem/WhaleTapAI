from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.main_menu_handler import (
    handle_main_menu,
    handle_subscription_info,
    handle_back_to_plans
)
from subscriptions.settings_handler import handle_settings
from subscriptions.auto_trading_handler import handle_auto_trading  # ← تم التصحيح هنا
from subscriptions.copy_trade_handler import handle_copy_trade
from subscriptions.language_handler import handle_language_change
from subscriptions.admin_handler import handle_admin_confirm_payment
from models.database import init_db
import os

# تهيئة قاعدة البيانات
init_db()

TOKEN = os.getenv("BOT_TOKEN")
application = Application.builder().token(TOKEN).build()

# أوامر البداية
application.add_handler(CommandHandler("start", handle_main_menu))

# الكولباك من الأزرار
application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
application.add_handler(CallbackQueryHandler(handle_back_to_plans, pattern="^back_to_plans$"))
application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
application.add_handler(CallbackQueryHandler(handle_auto_trading, pattern="^auto_trading$"))
application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))
application.add_handler(CallbackQueryHandler(handle_language_change, pattern="^lang_"))
application.add_handler(CallbackQueryHandler(handle_admin_confirm_payment, pattern="^admin_confirm_payment$"))

if __name__ == "__main__":
    application.run_polling()
