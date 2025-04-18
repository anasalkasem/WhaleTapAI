import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# إعداد اللوجر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# التوكن من متغيرات البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")  # ← التعديل هنا

if not BOT_TOKEN:
    raise ValueError("لم يتم تعيين BOT_TOKEN في متغيرات البيئة")

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
            "🚀 مرحبًا! اختر أحد الخيارات:",
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"خطأ في دالة start: {e}")
        await update.message.reply_text("⚠️ حدث خطأ، يرجى المحاولة لاحقًا")

async def handle_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "subscribe_pro":
        keyboard = [
            [InlineKeyboardButton("💳 دفع بـ SOL", callback_data="pay_sol")],
            [InlineKeyboardButton("💎 دفع بـ USDT", callback_data="pay_usdt")],
            [InlineKeyboardButton("↩ رجوع", callback_data="back_to_start")]
        ]
        await query.edit_message_text(
            text="اختر طريقة الدفع:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "subscribe_free":
        await query.edit_message_text(text="🎉 تم تفعيل الاشتراك المجاني بنجاح!")

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "pay_sol":
        await query.edit_message_text(
            text="🔷 الرجاء إرسال 20 SOL إلى العنوان:\n\n"
                 "SOL_Address_123...\n\n"
                 "✅ سيتم تفعيل اشتراكك خلال 10 دقائق من التأكيد"
        )
    elif query.data == "pay_usdt":
        await query.edit_message_text(
            text="💎 الرجاء إرسال 20 USDT (TRC20) إلى العنوان:\n\n"
                 "USDT_Address_123...\n\n"
                 "✅ سيتم تفعيل اشتراكك خلال 10 دقائق من التأكيد"
        )

async def handle_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

def main():
    try:
        application = Application.builder().token(BOT_TOKEN).build()

        # إضافة المعالجات
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(handle_subscription, pattern="^subscribe_"))
        application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
        application.add_handler(CallbackQueryHandler(handle_back, pattern="^back_to_start$"))

        logger.info("Starting the bot...")
        application.run_polling()

    except Exception as e:
        logger.critical(f"فشل تشغيل البوت: {e}")
        raise

if __name__ == "__main__":
    main()
