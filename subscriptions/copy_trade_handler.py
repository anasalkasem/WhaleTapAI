from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard
from models.database import Session, WhaleTrade
import datetime

# دالة تنفيذ نسخ صفقة الحوت
async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    lang = context.user_data.get("lang", "ar")

    session = Session()

    try:
        # صفقة وهمية
        fake_trade = WhaleTrade(
            user_id=user_id,
            whale_wallet="whale_fake_wallet_123",
            token_address="token_fake_address_456",
            amount=12345.67,
            trade_type="buy",
            timestamp=datetime.datetime.utcnow()
        )

        session.add(fake_trade)
        session.commit()

        if lang == "en":
            text = "✅ The whale trade has been copied successfully!"
        elif lang == "es":
            text = "✅ ¡La operación de la ballena se ha copiado con éxito!"
        else:
            text = "✅ تم نسخ صفقة الحوت بنجاح!"

    except Exception as e:
        session.rollback()
        print(f"[DB ERROR] Failed to copy trade: {e}")

        if lang == "en":
            text = "❌ An error occurred while copying the trade. Please try again later."
        elif lang == "es":
            text = "❌ Ocurrió un error al copiar la operación. Inténtalo de nuevo más tarde."
        else:
            text = "❌ حدث خطأ أثناء نسخ الصفقة. حاول لاحقاً."
    
    finally:
        session.close()

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=main_menu_keyboard(lang)
    )
