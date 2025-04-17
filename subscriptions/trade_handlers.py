from telegram import Update
from telegram.ext import ContextTypes
from utils.trade_utils import save_trade_data  # تم التعديل هنا

async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # صفقة وهمية للتجريب (سيتم استبدالها لاحقًا ببيانات من Helius API)
    fake_trade = {
        "wallet": "SolanaWhaleAddress111",
        "token": "BONK",
        "amount": 9543.22,
        "tx_type": "buy",
        "timestamp": "2024-04-16 12:00:00"
    }

    save_trade_data(
        user_id=user_id,
        wallet=fake_trade["wallet"],
        token=fake_trade["token"],
        amount=fake_trade["amount"],
        tx_type=fake_trade["tx_type"],
        timestamp=fake_trade["timestamp"]
    )

    await update.message.reply_text("✅ تم حفظ صفقة الحوت بنجاح (وهمية للتجريب).")
