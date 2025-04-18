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
    from subscriptions.payment_handlers import handle_pay_usdt
application.add_handler(CallbackQueryHandler(handle_pay_usdt, pattern="^pay_usdt_"))
from subscriptions.payment_handlers import handle_free_plan
application.add_handler(CallbackQueryHandler(handle_free_plan, pattern="^subscribe_free$"))
from subscriptions.stats_handler import handle_my_stats
application.add_handler(CallbackQueryHandler(handle_my_stats, pattern="^my_stats$"))
from subscriptions.settings_handler import handle_settings
application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
from subscriptions.insights_handler import handle_smart_insights
application.add_handler(CallbackQueryHandler(handle_smart_insights, pattern="^smart_insights$"))
from subscriptions.settings_handler import (
    handle_settings,
    handle_change_language,
    handle_language_selection
)

application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
application.add_handler(CallbackQueryHandler(handle_change_language, pattern="^change_language$"))
application.add_handler(CallbackQueryHandler(handle_language_selection, pattern="^lang_"))
