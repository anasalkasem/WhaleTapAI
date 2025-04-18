from telegram import Update
from telegram.ext import ContextTypes

async def handle_how_it_works(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "طريقة عمل البوت:\n\n"
        "- اختر خطة الاشتراك.\n"
        "- بعد التفعيل، اضغط على \"نسخ التداول\".\n"
        "- البوت سيبدأ تلقائيًا بمراقبة صفقات الحيتان ونسخها.\n"
        "- يمكنك أيضًا تشغيل التداول التلقائي، وإعداد حد خسارة."
    )
