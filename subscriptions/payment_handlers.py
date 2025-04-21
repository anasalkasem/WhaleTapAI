from telegram import Update
from telegram.ext import ContextTypes

# عرض عنوان محفظة الدفع بـ SOL (مترجم)
async def handle_pay_with_sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "ar")
    wallet_address = "YOUR_SOLANA_WALLET_ADDRESS"  # ← استبدله بعنوان محفظتك الحقيقي

    if lang == "en":
        text = (
            "💠 <b>To complete your payment:</b>\n"
            "Send exactly <code>1 SOL</code> to the address below:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 After sending, please send the transaction hash or screenshot to confirm."
        )
    elif lang == "es":
        text = (
            "💠 <b>Para completar tu pago:</b>\n"
            "Envía exactamente <code>1 SOL</code> a la siguiente dirección:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 Después del envío, por favor envía el hash de la transacción o una captura de pantalla para confirmar."
        )
    else:
        text = (
            "💠 <b>لإتمام عملية الدفع:</b>\n"
            "أرسل <code>1 SOL</code> إلى العنوان التالي:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 بعد التحويل، أرسل صورة أو Hash المعاملة لتأكيد التفعيل."
        )

    await query.edit_message_text(text=text, parse_mode="HTML")


# تفعيل النسخة المجانية (مترجم)
async def handle_free_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = context.user_data.get("lang", "ar")

    if lang == "en":
        text = (
            f"🆓 Free plan activated successfully!\n\n"
            f"Welcome {user.first_name}, you can now copy 1 trade per day.\n"
            f"Upgrade anytime to unlock full features."
        )
    elif lang == "es":
        text = (
            f"🆓 ¡Plan gratuito activado con éxito!\n\n"
            f"Bienvenido {user.first_name}, ahora puedes copiar 1 operación por día.\n"
            f"Actualiza cuando quieras para desbloquear todas las funciones."
        )
    else:
        text = (
            f"🆓 تم تفعيل النسخة المجانية بنجاح!\n\n"
            f"مرحباً {user.first_name}، يمكنك الآن نسخ صفقة واحدة يومياً.\n"
            f"قم بالترقية لاحقاً للاستفادة الكاملة من المميزات."
        )

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)
from telegram import Update
from telegram.ext import ContextTypes

# عرض عنوان محفظة الدفع بـ SOL
async def handle_pay_with_sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "ar")
    wallet_address = "GdUperqSSz4QJd2xGMmot1JGRU9n6wpWNzEbMBTbs5Wp"

    if lang == "en":
        text = (
            "💠 <b>To complete your payment:</b>\n"
            "Send exactly <code>1 SOL</code> to the address below:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 After sending, please send the transaction hash or screenshot to confirm."
        )
    elif lang == "es":
        text = (
            "💠 <b>Para completar tu pago:</b>\n"
            "Envía exactamente <code>1 SOL</code> a la siguiente dirección:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 Después del envío, por favor envía el hash de la transacción o una captura de pantalla para confirmar."
        )
    else:
        text = (
            "💠 <b>لإتمام عملية الدفع:</b>\n"
            "أرسل <code>1 SOL</code> إلى العنوان التالي:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 بعد التحويل، أرسل صورة أو Hash المعاملة لتأكيد التفعيل."
        )

    await query.edit_message_text(text=text, parse_mode="HTML")
from sqlalchemy import Column, Integer, BigInteger, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class PaymentRequest(Base):
    __tablename__ = "payment_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)  # رقم تعريفي فريد
    user_id = Column(BigInteger, nullable=False)                # معرف المستخدم على تيليجرام
    username = Column(String, nullable=True)                    # اسم المستخدم (اختياري)
    wallet_address = Column(String, nullable=False)             # عنوان محفظتك (مثلاً: SOL)
    amount = Column(Float, nullable=False)                      # المبلغ المطلوب دفعه
    status = Column(String, default="pending")                  # الحالة: pending / confirmed / rejected
    created_at = Column(DateTime, default=datetime.datetime.utcnow)  # وقت الإنشاء
