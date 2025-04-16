from telegram import Update
from telegram.ext import ContextTypes
from .subscription_plans import PLANS
from .db_utils import save_payment

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    _, plan, currency = query.data.split('_')
    await query.edit_message_text(
        text=f"💳 الدفع عبر {currency}\n🔷 المبلغ: {PLANS[plan]['price']} {currency}\n🪙 المحفظة: `{get_wallet_address(currency)}`",
        parse_mode="Markdown"
    )
    save_payment(query.from_user.id, plan, currency, PLANS[plan]['price'])

def get_wallet_address(currency: str) -> str:
    wallets = {
        "SOL": "So1ANaWalletAddress123456789",
        "USDT": "TetherERC20Address123456789"
    }
    return wallets.get(currency, "")