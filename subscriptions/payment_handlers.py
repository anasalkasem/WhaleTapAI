from telegram import Update
from telegram.ext import ContextTypes

# معالجة زر الدفع بـ SOL
async def handle_pay_sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    wallet_address = "YOUR_SOLANA_WALLET_ADDRESS"  # استبدلها بعنوان محفظتك

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=f"💠 للدفع باستخدام عملة SOL:\n\n"
             f"• المبلغ: 1 SOL\n"
             f"• العنوان: `{wallet_address}`\n\n"
             f"📌 بعد التحويل، أرسل صورة أو Hash المعاملة لتأكيد التفعيل.",
        parse_mode="Markdown"
    )
# معالجة زر الدفع بـ USDT
async def handle_pay_usdt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdt_wallet = "YOUR_USDT_WALLET_ADDRESS"  # استبدلها بعنوان محفظتك

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=f"💎 للدفع باستخدام USDT (شبكة TRC20):\n\n"
             f"• السعر: 20 USDT\n"
             f"• العنوان: `{usdt_wallet}`\n\n"
             f"📌 بعد التحويل، أرسل صورة أو Hash المعاملة لتأكيد التفعيل.",
        parse_mode="Markdown"
    )
# تفعيل النسخة المجانية
async def handle_free_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=f"🆓 تم تفعيل النسخة المجانية بنجاح!\n\n"
             f"مرحباً {user.first_name}، يمكنك الآن نسخ صفقة واحدة يومياً.\n"
             f"قم بالترقية لاحقاً للاستفادة الكاملة من المميزات.",
    )

    # (اختياري) أضف المستخدم إلى قاعدة البيانات كـ "Free"
