from telegram import Update
from telegram.ext import ContextTypes
from database import SessionLocal
from models.models import WhaleTrade, Subscription

# دالة حفظ صفقة عند نسخها - بشرط اشتراك PRO فقط
async def handle_copy_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = context.user_data.get("lang", "ar")

    db = SessionLocal()
    subscription = db.query(Subscription).filter_by(user_id=user.id).first()

    if not subscription or subscription.plan_type != "pro":
        # رسالة الرفض للمستخدم المجاني
        if lang == "en":
            text = "⚠️ This feature is available for PRO users only.\nPlease upgrade your plan to copy whale trades."
        elif lang == "es":
            text = "⚠️ Esta función está disponible solo para usuarios PRO.\nActualiza tu plan para copiar operaciones de ballenas."
        else:
            text = "⚠️ هذه الميزة متاحة فقط لمشتركي PRO.\nيرجى الترقية لنسخ صفقات الحيتان."

        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text)
        db.close()
        return

    # إذا كان PRO، ننسخ الصفقة
    fake_trade = WhaleTrade(
        user_id=user.id,
        whale_wallet="3xWhaleSOLwallet999",
        token_address="So11111111111111111111111111111111111111112",
        amount=2.5,
        trade_type="buy"
    )

    db.add(fake_trade)
    db.commit()
    db.close()

    if lang == "en":
        text = "✅ Trade copied!\nYou copied a whale buying 2.5 SOL."
    elif lang == "es":
        text = "✅ ¡Has copiado una operación!\nBallena comprando 2.5 SOL."
    else:
        text = "✅ تم نسخ الصفقة بنجاح!\nلقد قمت بنسخ صفقة حوت اشترى 2.5 SOL."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)
