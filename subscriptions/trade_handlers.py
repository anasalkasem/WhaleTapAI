from telegram import Update
from telegram.ext import ContextTypes
from utils.trade_utils import save_trade_data

async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("تم الضغط على زر نسخ الصفقة")  # للمراقبة من Railway

    await update.callback_query.answer()  # لإزالة "جار التحميل"

    user_id = update.effective_user.id

    # بيانات وهمية للصفقة
    fake_trade = {
        "wallet": "SolanaWhaleAddress111",
        "token": "BONK",
        "amount": 9543.22,
        "tx_type": "buy",
        "timestamp": "2024-04-16 12:00:00"
    }

    # حفظ الصفقة في قاعدة البيانات
    save_trade_data(
        user_id=user_id,
        wallet=fake_trade["wallet"],
        token=fake_trade["token"],
        amount=fake_trade["amount"],
        tx_type=fake_trade["tx_type"],
        timestamp=fake_trade["timestamp"]
    )

    await update.callback_query.message.reply_text("✅ تم حفظ صفقة الحوت بنجاح (وهمية للتجريب).")
