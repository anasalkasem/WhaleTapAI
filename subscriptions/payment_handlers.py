from telegram import Update
from telegram.ext import ContextTypes

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id

    # رسالة توضح أن التحقق سيتم يدويًا
    await query.edit_message_text(
        "تم استلام طلب الاشتراك الخاص بك.\n"
        "سيتحقق المسؤول من الدفع ويفعّل حسابك خلال وقت قصير."
    )

    # إرسال إشعار إلى الأدمن
    admin_id = int(os.getenv("ADMIN_ID"))
    await context.bot.send_message(
        chat_id=admin_id,
        text=f"طلب اشتراك جديد من المستخدم: {user_id}\nيرجى التحقق يدويًا وتفعيل الاشتراك إن كان الدفع صحيح."
    )
