
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.keyboards import plans_keyboard
from subscriptions.payment_handlers import handle_payment, handle_plan_selection
from subscriptions.db_utils import init_db

async def start(update, context):
    await update.message.reply_text(
        "🎟️ اختر باقة الاشتراك:",
        reply_markup=plans_keyboard()
    )

def main():
    init_db()
    app = Application.builder().token("YOUR_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_plan_selection, pattern="^plan_"))
    app.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    app.run_polling()

if __name__ == "__main__":
    main()
