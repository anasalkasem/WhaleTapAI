from telegram import Update
from telegram.ext import ContextTypes
from utils.trade_utils import save_trade_data  # تأكد من المسار الصحيح

async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id

        # بيانات وهمية مؤقتة
        fake_trade = {
            "wallet": "So1anaWhaleAddress111",
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

        await update.callback_query.answer()
        await update.callback_query.edit_message_text("✅ تم نسخ الصفقة التجريبية وحفظها بنجاح.")
    
    except Exception as e:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(f"❌ حدث خطأ أثناء نسخ الصفقة: {e}")
