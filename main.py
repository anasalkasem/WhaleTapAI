import os
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ContextTypes
)
from subscriptions.db_utils import activate_subscription
from subscriptions.keyboards import plans_keyboard
from subscriptions.payment_handlers import handle_payment
from subscriptions.trade_handlers import handle_copy_trade

# تحقق من وجود المتغيرات الأساسية
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")

# أدمن البوت
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
        success = activate_subscription(user_id)
        if success:
            await update.message.reply_text(f"✅ تم تفعيل اشتراك المستخدم {user_id}.")
            # يمكنك إرسال إشعار للمستخدم هنا
        else:
            await update.message.reply_text(f"⚠️ لم يتم العثور على المستخدم {user_id}")
    except ValueError:
        await update.message.reply_text("⚠️ يجب أن يكون المعرف رقماً صحيحاً")
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {str(e)}")

def main():
    try:
        app = Application.builder().token(TOKEN).build()

        # أوامر البوت
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("activate", activate))
        app.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_"))
        app.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))

        # اختر أحد الخيارين: Webhook أو Polling
        
        # الخيار 1: التشغيل بـ Webhook (يتطلب SSL)
        if os.getenv("WEBHOOK_MODE", "false").lower() == "true":
            domain = os.getenv("DOMAIN")
            cert_path = os.getenv("CERT_PATH")
            if not domain or not cert_path:
                raise ValueError("يجب تعيين DOMAIN وCERT_PATH لاستخدام Webhook")
            
            app.run_webhook(
                listen="0.0.0.0",
                port=int(os.getenv("PORT", 8443)),
                webhook_url=f"{domain}/webhook",
                cert=cert_path
            )
        
        # الخيار 2: التشغيل بـ Polling (للتطوير)
        else:
            print("Bot is running in polling mode...")
            app.run_polling()

    except Exception as e:
        print(f"فشل تشغيل البوت: {str(e)}")

if __name__ == "__main__":
    main()
