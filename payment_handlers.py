
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from .db_utils import save_payment
from .subscription_plans import PLANS
from .keyboards import crypto_payment_keyboard

async def handle_plan_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    plan = query.data.split("_")[-1]
    await query.edit_message_text(
        text=f"اختر طريقة الدفع لاشتراك {plan.upper()}:",
        reply_markup=crypto_payment_keyboard(plan)
    )

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    _, plan, currency = query.data.split('_')
    await query.edit_message_text(
        text=f"""
💳 *طريقة الدفع: {currency}*
🪙 **المبلغ:** {PLANS[plan]['price']} {currency}
📦 **الباقة:** {plan.upper()}
🔷 **المحفظة:** `{get_wallet_address(currency)}`
⏳ سيتم التفعيل خلال 10 دقائق من التأكيد
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
        "SOL": "So1ANaWalletAddress123456789",
        "USDT": "TetherERC20Address123456789"
    }
    return wallets.get(currency, "")
