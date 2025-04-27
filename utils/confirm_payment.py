# utils/confirm_payment.py

from utils.save_payment import save_payment_request

WALLET_ADDRESS = "GdUperqSSz4QJd2xGMmot1JGRU9n6wpWNzEbMBTbs5Wp"

async def handle_subscribe_pro(update, context):
    query = update.callback_query
    user = query.from_user
    user_id = user.id
    username = user.username or "Unknown"

    await query.answer()

    # Save payment request in the database
    await save_payment_request(user_id, username, WALLET_ADDRESS, 20.0)

    # Send payment instructions to the user
    await query.edit_message_text(
        text=(
            "✅ Your subscription request has been registered!\n\n"
            "Please send **20 USDC-SPL** to the following wallet address:\n\n"
            f"`{WALLET_ADDRESS}`\n\n"
            "After the transfer, your subscription will be activated shortly."
        ),
        parse_mode="Markdown"
    )
