from telegram import Update
from telegram.ext import ContextTypes
from database import SessionLocal
from models.models import WhaleTrade

# دالة حفظ صفقة وهمية عند نسخ الصفقة
async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = context.user_data.get("lang", "ar")

    # بيانات صفقة وهمية
    fake_trade = WhaleTrade(
        user_id=user.id,
        whale_wallet="3xWhaleSOLwallet999",
        token_address="So11111111111111111111111111111111111111112",
        amount=2.5,
        trade_type="buy"
    )

    # حفظ الصفقة في قاعدة البيانات
    db = SessionLocal()
    db.add(fake_trade)
    db.commit()
    db.close()

    # رسالة تأكيد حسب اللغة
    if lang == "en":
        text = "✅ Trade copied!\nYou copied a whale buying 2.5 SOL."
    elif lang == "es":
        text = "✅ ¡Has copiado una operación!\nBallena comprando 2.5 SOL."
    else:
        text = "✅ تم نسخ الصفقة بنجاح!\nلقد قمت بنسخ صفقة حوت اشترى 2.5 SOL."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)
