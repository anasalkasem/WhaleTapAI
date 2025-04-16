async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data

    if data == "free_plan":
        # تفعيل مباشر
        update_user_subscription(user_id, "free", "active")
        await query.edit_message_text("✅ تم تفعيل الباقة المجانية. يمكنك الآن نسخ صفقة واحدة يوميًا.")
    elif data.startswith("pay_"):
        _, plan, currency = data.split("_")
        await query.edit_message_text(
            f"""
💳 *طريقة الدفع: {currency}*
-
🪙 **المبلغ:** {PLANS[plan]['price']} {currency}
📦 **الباقة:** {plan.upper()}
🔷 **المحفظة:** `{get_wallet_address(currency)}`
-
⏳ *تم استلام طلبك وسيتم التفعيل بعد التأكيد اليدوي.*
""",
            parse_mode="Markdown"
        )
        save_payment(user_id, plan, currency, PLANS[plan]["price"])
