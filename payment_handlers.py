import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from .db_utils import save_payment
from .subscription_plans import PLANS

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    _, plan, currency = query.data.split('_')

    await query.edit_message_text(
        text=f"طريقة الدفع: {currency}\n"
             f"المبلغ: {PLANS[plan]['price']} {currency}\n"
             f"الباقة: {plan.upper()}\n"
             f"المحفظة: {get_wallet_address(currency)}\n"
             f"⏳ سيتم التفعيل خلال 10 دقائق من التأكيد",
        parse_mode="Markdown"
    )

    save_payment(
        user_id=query.from_user.id,
        plan=plan,
        currency=currency,
        amount=PLANS[plan]['price']
    )

def get_wallet_address(currency: str) -> str:
    wallets = {
        "SOL": "So1ANaWalletAddress123456789",
        "USDT": "TetherERC20Address123456789"
    }
    return wallets.get(currency, "")
