
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from subscriptions.keyboards import plans_keyboard
from subscriptions.payment_handlers import handle_payment

async def start(update, context):
    await update.message.reply_text("اختر خطتك:", reply_markup=plans_keyboard())

app = Application.builder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
app.run_polling()
