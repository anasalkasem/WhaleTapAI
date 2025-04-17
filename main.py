import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from subscriptions.subscription_handlers import handle_subscription_choice
from subscriptions.payment_handlers import handle_payment
from subscriptions.trade_handlers import handle_copy_trade

# إعداد اللوجر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# التوكن - الأفضل استخدام متغيرات البيئة
BOT_TOKEN = "YOUR_BOT_TOKEN"  # استبدلها بالتوكن الفعلي

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        keyboard = [
            [
                InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro"),
                InlineKeyboardButton("🆓 اشتراك مجاني", callback_data="subscribe_free")
            ],
            [
                InlineKeyboardButton("⏬ نسخ الصفقة الآن", callback_data="copy_trade")
            ]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🚀 اختر باقة الاشتراك المناسبة:",
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Error in start handler: {e}")
        await update.message.reply_text("⚠️ حدث خطأ، يرجى المحاولة لاحقًا")

def main():
    try:
        if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN":
            raise ValueError("لم يتم تعيين توكن البوت")
        
        application = Application.builder().token(BOT_TOKEN).build()

        # إضافة المعالجات
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(handle_subscription_choice, pattern=r"^subscribe_(pro|free)$"))
        application.add_handler(CallbackQueryHandler(handle_payment, pattern=r"^pay_(sol|usdt)_"))
        application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))

        logger.info("Starting bot...")
        application.run_polling()

    except Exception as e:
        logger.critical(f"Bot failed: {e}")
        raise

if __name__ == "__main__":
    main()
