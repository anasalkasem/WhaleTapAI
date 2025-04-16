from telegram import Update
from telegram.ext import ContextTypes
from .db_utils import save_payment
from .subscription_plans import PLANS

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    _, plan, currency = query.data.split('_')

    wallet = get_wallet_address(currency)
    await query.edit_message_text(
        text=f"💳 *طريقة الدفع:* {currency}\n"
             f"🪙 **المبلغ:** {PLANS[plan]['price']} {currency}\n"
             f"📦 **الباقة:** {plan.upper()}\n"
             f"🔷 **المحفظة:** `{wallet}`\n"
             f"⏳ سيتم التفعيل خلال 10 دقائق بعد التأكيد.",
        parse_mode="Markdown"
    )
    save_payment(query.from_user.id, plan, currency, PLANS[plan]["price"])

def get_wallet_address(currency: str) -> str:
    wallets = {
        "SOL": "So1ANaWalletAddress123456789",
        "USDT": "TetherERC20Address123456789"
    }
    return wallets.get(currency, "")
    await query.edit_message_text(
    text="✅ تم استلام بيانات الدفع.\nسيتم التحقق يدويًا وتفعيل اشتراكك خلال 10 دقائق.\nشكراً لك!",
)
