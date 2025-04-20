import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from db_utils import init_db

from subscriptions.main_menu_handler import (
    handle_main_menu,
    handle_subscription_info,
    handle_back_to_plans,
)
from subscriptions.payment_handlers import (
    handle_pay_with_sol,
    handle_free_plan,
)
from subscriptions.stats_handler import handle_my_stats
from subscriptions.settings_handler import (
    handle_settings,
    handle_change_language,
    handle_language_selection,
    handle_toggle_notifications,
)
from subscriptions.insights_handler import handle_smart_insights
from subscriptions.how_it_works_handler import handle_how_it_works
from subscriptions.copy_trade_handler import handle_copy_trade
from subscriptions.auto_trading_handlers import (
    handle_auto_trading,
    handle_stop_copying
)
from utils.delete_table_whale_trades_v2 import handle_delete_trades  # للأدمن فقط

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # أضف هذا المتغير في Railway

def main():
    init_db()

    application = Application.builder().token(TOKEN).build()

    # الأوامر
    application.add_handler(CommandHandler("start", handle_main_menu))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
    application.add_handler(CallbackQueryHandler(handle_back_to_plans, pattern="^back_to_plans$"))
    application.add_handler(CallbackQueryHandler(handle_free_plan, pattern="^subscribe_free$"))
    application.add_handler(CallbackQueryHandler(handle_pay_with_sol, pattern="^pay_sol_pro$"))
    application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
    application.add_handler(CallbackQueryHandler(handle_change_language, pattern="^change_language$"))
    application.add_handler(CallbackQueryHandler(handle_language_selection, pattern="^lang_"))
    application.add_handler(CallbackQueryHandler(handle_toggle_notifications, pattern="^toggle_notifications$"))
    application.add_handler(CallbackQueryHandler(handle_my_stats, pattern="^my_stats$"))
    application.add_handler(CallbackQueryHandler(handle_smart_insights, pattern="^smart_insights$"))
    application.add_handler(CallbackQueryHandler(handle_how_it_works, pattern="^how_it_works$"))
    application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))
    application.add_handler(CallbackQueryHandler(handle_delete_trades, pattern="^admin_delete_trades$"))

    # أوامر التداول التلقائي
    application.add_handler(CallbackQueryHandler(handle_auto_trading, pattern="^auto_trading$"))
    application.add_handler(CallbackQueryHandler(handle_stop_copying, pattern="^stop_copying$"))

    # ✅ تشغيل Webhook بدل polling
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    main()
