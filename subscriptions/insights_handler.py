from telegram import Update
from telegram.ext import ContextTypes
from subscriptions.keyboards import main_menu_keyboard

async def handle_smart_insights(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🧠 <b>Smart Whale Insights</b>\n\n"
        "📍 أبرز نشاطات الحيتان خلال الـ24 ساعة الماضية:\n\n"
        "• حوت 0xA1...2F قام بشراء 120,000 SOL\n"
        "• حوت 0xB9...C3 نقل 50,000 USDT إلى منصة Binance\n"
        "• 3 حيتان جدد انضموا إلى السوق اليوم\n\n"
        "💡 تابع هذه التحركات، وابقَ على اطلاع لتنسخ صفقات الحيتان الأذكى!"
    )

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text, reply_markup=main_menu_keyboard(), parse_mode="HTML")
