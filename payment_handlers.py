from telegram import Update
from telegram.ext import ContextTypes
from .subscription_plans import PLANS
from .keyboards import crypto_payment_keyboard
from .db_utils import save_payment

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    _, plan, currency = query.data.split('_')

    await query.edit_message_text(
        text=f"""
Payment Method: {currency}
Plan: {plan.upper()}
Price: {PLANS[plan]['price']} {currency}
Wallet Address: `{get_wallet_address(currency)}`
After sending the payment, your subscription will be activated soon.
""",
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
        "USDT": "TetherUSDTWallet123...",
        "SOL": "SolanaWalletABC123..."
    }
    return wallets.get(currency, "Unknown")
