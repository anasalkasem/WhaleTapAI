from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard
from models.database import get_db, WhaleTrade  # تصحيح الاستيراد

# دالة تنفيذ نسخ صفقة الحوت
async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    lang = context.user_data.get("lang", "ar")

    db = get_db()

    try:
        fake_trade = WhaleTrade(
            user_id=user_id,
            whale_wallet="3xWhaleSOLwallet999",
            token_address="So11111111111111111111111111111111111111112",
            amount=2.5,
            trade_type="buy"
        )

        db.add(fake_trade)
        db.commit()

        if lang == "en":
            text = "✅ Whale trade copied successfully!"
        elif lang == "es":
            text = "✅ ¡Has copiado la operación de la ballena con éxito!"
        else:
            text = "✅ تم نسخ صفقة الحوت بنجاح!"
    except Exception as e:
        print("❌ DB Error:", e)
        text = "❌ حدث خطأ أثناء نسخ الصفقة. حاول لاحقًا."
    finally:
        db.close()

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=main_menu_keyboard(lang)
    )
