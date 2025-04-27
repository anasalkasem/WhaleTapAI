from utils.save_payment import save_payment_request
from utils.payment_utils import has_pending_payment  # <-- جديد هذا
WALLET_ADDRESS = "GdUperqSSz4QJd2xGMmot1JGRU9n6wpWNzEbMBTbs5Wp"

async def handle_subscribe_pro(update, context):
    query = update.callback_query
    user = query.from_user
    user_id = user.id
    username = user.username or "Unknown"

    await query.answer()

    # تحقق هل لديه طلب دفع معلق
    if has_pending_payment(user_id):
        await query.edit_message_text(
            text="⚠️ You already have a pending subscription request.\n\nPlease complete the payment first!",
            parse_mode="Markdown"
        )
        return  # نوقف هنا وما نرسل عنوان المحفظة مرة ثانية

    # إذا ما عنده طلب دفع معلق، نكمل ونحفظ الطلب
    save_payment_request(user_id, username, WALLET_ADDRESS)

    await query.edit_message_text(
        text=(
            "✅ Your subscription request has been registered!\n\n"
            "Please send **20 USDC-SPL** to the following wallet address:\n\n"
            f"`{WALLET_ADDRESS}`\n\n"
            "After the transfer, your subscription will be activated shortly."
        ),
        parse_mode="Markdown"
    )
