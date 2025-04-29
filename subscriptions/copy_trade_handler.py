from telegram import Update
from telegram.ext import ContextTypes
from models.database import SessionLocal, WhaleTrade
from subscriptions.keyboards import main_menu_keyboard
import datetime
import logging

# إعداد اللوج
logger = logging.getLogger(__name__)

# تنفيذ نسخ الصفقة
async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = context.user_data.get("lang", "ar")

    try:
        session = SessionLocal()

        # صفقة وهمية
        fake_trade = WhaleTrade(
            user_id=user_id,
            whale_wallet="fake_wallet_123",
            token_address="fake_token_abc",
            amount=1234.56,
            trade_type="buy",
            timestamp=datetime.datetime.utcnow()
        )

        session.add(fake_trade)
        session.commit()
        session.close()

        # نجاح
        if lang == "en":
            text = "✅ The whale trade has been copied successfully!"
        elif lang == "es":
            text = "✅ ¡La operación de la ballena se ha copiado con éxito!"
        else:
            text = "✅ تم نسخ صفقة الحوت بنجاح!"

    except Exception as e:
        logger.error(f"Error copying trade: {e}")  # يسجل الخطأ
        if lang == "en":
            text = "❌ An error occurred while copying the trade. Please try again later."
        elif lang == "es":
            text = "❌ Se produjo un error al copiar la operación. Inténtalo más tarde."
        else:
            text = "❌ حدث خطأ أثناء نسخ الصفقة. حاول لاحقاً."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=main_menu_keyboard(lang, user_id),
    )
