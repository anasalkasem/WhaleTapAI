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

    # حذف Webhook الحالي لتفادي التعارض
    application.bot.delete_webhook()

    # ✅ تشغيل Webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        webhook_url=WEBHOOK_URL
    )
