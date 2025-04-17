from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import crypto_payment_keyboard
from .db_utils import save_payment
from .subscription_plans import PLANS

async def handle_subscription_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "subscribe_pro":
        await query.edit_message_text(
            "💰 يرجى اختيار وسيلة الدفع:",
            reply_markup=crypto_payment_keyboard("pro")
        )

    elif data == "subscribe_free":
        success = save_payment(
            user_id=query.from_user.id,
            plan="free",
            payment_method="auto",
            amount=0,
            status="active"
        )
        if success:
            await query.edit_message_text(
                "🎉 تم تفعيل اشتراكك المجاني (صفقة واحدة يوميًا).\n"
                "لترقية الاشتراك استخدم /upgrade"
            )
        else:
            await query.edit_message_text("⚠️ حدث خطأ أثناء التفعيل، يرجى المحاولة لاحقًا")
    else:
        await query.edit_message_text("🚫 خيار غير معروف")



async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data.startswith("pay_"):
        try:
            parts = data.split('_')
            if len(parts) >= 3:
                currency = parts[1]  # sol أو usdt
                plan = parts[2]     # pro أو غيرها

                if plan not in PLANS:
                    await query.edit_message_text("🚫 الخطة المطلوبة غير موجودة.")
                    return

                amount = PLANS[plan]["price"]

                success = save_payment(
                    user_id=user_id,
                    plan=plan,
                    payment_method=currency,
                    amount=amount,
                    status="pending"
                )

                if success:
                    await query.edit_message_text(
                        f"💳 تم استلام طلب الاشتراك ({plan.upper()})\n"
                        f"🔷 الرجاء إرسال {amount} {currency.upper()} إلى المحفظة\n"
                        "✅ ستصلك رسالة تأكيد عند اكتمال الدفع"
                    )
                else:
                    await query.edit_message_text("⚠️ فشل في تسجيل الطلب، يرجى المحاولة لاحقًا")
            else:
                await query.edit_message_text("🚫 البيانات غير مفهومة")
        except Exception as e:
            print(f"Error in payment handling: {e}")
            await query.edit_message_text("🚫 حدث خطأ غير متوقع، يرجى إعادة المحاولة")
