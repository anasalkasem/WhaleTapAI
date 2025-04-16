
from telegram import Update
from telegram.ext import ContextTypes
from .subscription_plans import PLANS
from .db_utils import save_payment

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    _, plan, currency = query.data.split('_')
    await query.edit_message_text(
        text=f"💳 ادفع {PLANS[plan]['price']} {currency}\n"
             f"🔹 المحفظة: `YourWalletAddressHere`",
        parse_mode="Markdown"
    )
    save_payment(query.from_user.id, plan, currency, PLANS[plan]['price'])
