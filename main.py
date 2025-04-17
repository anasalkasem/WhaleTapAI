import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from subscriptions.db_utils import activate_subscription
from subscriptions.keyboards import plans_keyboard
from subscriptions.payment_handlers import handle_payment
from subscriptions.trade_handlers import handle_copy_trade

# ضع معرفك هنا (Telegram User ID الخاص بك كأدمن)
ADMIN_ID = 6672291052

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎟️ اختر باقة الاشتراك:",
        reply_markup=plans_keyboard()
    )

async def activate(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("activate", activate))
    app.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    app.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))

    app.run_polling()

if __name__ == "__main__":
    main()
