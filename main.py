import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.keyboards import plans_keyboard
from subscriptions.payment_handlers import handle_payment
from subscriptions.db_utils import activate_subscription
from subscriptions.trade_handlers import handle_copy_trade  # وظيفة نسخ الصفقة

# معرف الأدمن
ADMIN_ID = 6672291052

# أمر /start لعرض الاشتراكات
async def start(update, context):
    await update.message.reply_text(
        "🎟️ اختر باقة الاشتراك:",
        reply_markup=plans_keyboard()
    )

# أمر /activate لتفعيل اشتراك يدوي من قبل الأدمن
async def activate(update, context):
    if update.effective_user.id != ADMIN_ID:
        return await update.message.reply_text("❌ ليس لديك صلاحية.")

    if not context.args:
        return await update.message.reply_text("يرجى كتابة معرف المستخدم.\nمثال: /activate 123456789")

    try:
        user_id = int(context.args[0])
        activate_subscription(user_id)
        await update.message.reply_text(f"✅ تم تفعيل اشتراك المستخدم {user_id}.")
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {str(e)}")

def main():
    app = Application.builder().token(os.getenv("TOKEN")).build()

    # الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("activate", activate))

    # أوامر الدفع
    app.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))

    # زر نسخ صفقة الحوت
    app.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))
    app.add_handler(CommandHandler("copy", handle_copy_trade))  # إذا كتب المستخدم /copy

    app.run_polling()

if __name__ == "__main__":
    main()
