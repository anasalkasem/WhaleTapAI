from telegram import Update
from telegram.ext import ContextTypes
from models.database import Session
from models.payment_requests import PaymentRequest
import datetime

# عرض عنوان محفظة الدفع وحفظ الطلب في قاعدة البيانات
async def handle_pay_with_sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "ar")
    wallet_address = "GdUperqSSz4QJd2xGMmot1JGRU9n6wpWNzEbMBTbs5Wp"
    amount = 1.0

    user = update.effective_user
    user_id = user.id
    username = user.username or None

    session = Session()
    new_request = PaymentRequest(
        user_id=user_id,
        username=username,
        wallet_address=wallet_address,
        amount=amount,
        status="pending",
        created_at=datetime.datetime.utcnow()
    )
    session.add(new_request)
    session.commit()
    session.close()

    if lang == "en":
        text = (
            "💠 <b>To complete your payment:</b>\n"
            "Send exactly <code>1 SOL</code> to the address below:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 After sending, send the transaction hash or screenshot to confirm."
        )
    elif lang == "es":
        text = (
            "💠 <b>Para completar tu pago:</b>\n"
            "Envía exactamente <code>1 SOL</code> a la siguiente dirección:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 Después del envío, envía el hash o una captura para confirmar."
        )
    else:
        text = (
            "💠 <b>لإتمام عملية الدفع:</b>\n"
            "أرسل <code>1 SOL</code> إلى العنوان التالي:\n\n"
            f"<code>{wallet_address}</code>\n\n"
            "📌 بعد التحويل، أرسل صورة أو Hash المعاملة لتأكيد التفعيل."
        )

    await query.edit_message_text(text=text, parse_mode="HTML")


# تفعيل النسخة المجانية
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
            f"Bienvenido {user.first_name}, ahora puedes copiar 1 operación por día."
        )
    else:
        text = (
            f"🆓 تم تفعيل النسخة المجانية بنجاح!\n\n"
            f"مرحباً {user.first_name}، يمكنك الآن نسخ صفقة واحدة يومياً."
        )

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)
from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import crypto_payment_keyboard

# عرض كيبورد الدفع عند اختيار اشتراك PRO
async def handle_subscribe_pro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "ar")
    keyboard = crypto_payment_keyboard(plan="pro", lang=lang)

    if lang == "en":
        text = "Choose your preferred payment method below:"
    elif lang == "es":
        text = "Elige tu método de pago preferido:"
    else:
        text = "اختر طريقة الدفع التي تفضلها:"

    await query.edit_message_text(text=text, reply_markup=keyboard)
