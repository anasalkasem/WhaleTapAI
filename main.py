import os
# import models.fix_whale_trades_v2  # تم التعليق بعد تنفيذ المهمة لمرة واحدة فقط
# import models.init_db  # تم التعليق بعد إنشاء الجداول لمرة واحدة فقط

from telegram.ext import Application, CommandHandler, CallbackQueryHandler

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
from utils.delete_table_whale_trades_v2 import handle_delete_trades  # تم إضافته

TOKEN = os.getenv("BOT_TOKEN")

def main():
    application = Application.builder().token(TOKEN).build()

    # أوامر البوت
    application.add_handler(CommandHandler("start", handle_main_menu))

    # القائمة الرئيسية
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    # الاشتراكات
    application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
    application.add_handler(CallbackQueryHandler(handle_back_to_plans, pattern="^back_to_plans$"))
    application.add_handler(CallbackQueryHandler(handle_free_plan, pattern="^subscribe_free$"))

    # الدفع بـ SOL فقط
    application.add_handler(CallbackQueryHandler(handle_pay_with_sol, pattern="^pay_sol_pro$"))

    # الإعدادات واللغة والتنبيهات
    application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
    application.add_handler(CallbackQueryHandler(handle_change_language, pattern="^change_language$"))
    application.add_handler(CallbackQueryHandler(handle_language_selection, pattern="^lang_"))
    application.add_handler(CallbackQueryHandler(handle_toggle_notifications, pattern="^toggle_notifications$"))

    # الإحصائيات والرؤية الذكية
    application.add_handler(CallbackQueryHandler(handle_my_stats, pattern="^my_stats$"))
    application.add_handler(CallbackQueryHandler(handle_smart_insights, pattern="^smart_insights$"))

    # كيف يعمل البوت؟
    application.add_handler(CallbackQueryHandler(handle_how_it_works, pattern="^how_it_works$"))

    # نسخ الصفقة
    application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))

    # حذف سجل الصفقات (للأدمن فقط)
    application.add_handler(CallbackQueryHandler(handle_delete_trades, pattern="^admin_delete_trades$"))

    application.run_polling()

if __name__ == "__main__":
    main()
