from utils.db_utils import save_payment_request  # تصحيح مسار الاستيراد

# Your SOL wallet address
WALLET_ADDRESS = "GdUperqSSz4QJd2xGMmot1JGRU9n6wpWNzEbMBTbs5Wp"

async def handle_subscribe_pro(update, context):
    user_id = update.callback_query.from_user.id
    query = update.callback_query

    await query.answer()

    # Save payment request in the database
    await save_payment_request(user_id)

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
