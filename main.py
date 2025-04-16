from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.keyboards import plans_keyboard
from subscriptions.payment_handlers import handle_payment

async def start(update, context):
    await update.message.reply_text(
        "🎟️ اختر باقة الاشتراك:",
        reply_markup=plans_keyboard()
    )

def main():
    app = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
    app.run_polling()

if __name__ == "__main__":
    main()