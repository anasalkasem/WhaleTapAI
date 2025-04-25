from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import Session
from models.payment_requests import PaymentRequest

ADMIN_ID = 6672291052

def main_menu_keyboard(lang="en", user_id=None):
    session = Session()
    has_pending_payment = False

    if user_id == ADMIN_ID:
        has_pending_payment = session.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first() is not None

    session.close()

    buttons = []

    if lang == "en":
        buttons = [
            [InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")],
            [InlineKeyboardButton("📈 Copy Latest Trade", callback_data="copy_trade"),
             InlineKeyboardButton("🧠 Smart Whale Insights", callback_data="smart_insights")],
            [InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
             InlineKeyboardButton("📊 My Portfolio", callback_data="my_stats")],
            [InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
             InlineKeyboardButton("💳 Upgrade to PRO", callback_data="subscribe_pro")],
            [InlineKeyboardButton("🆓 Free Plan", callback_data="subscribe_free")]
        ]
    elif lang == "es":
        buttons = [
            [InlineKeyboardButton("🤖 Trading automático", callback_data="auto_trading")],
            [InlineKeyboardButton("📈 Copiar la última operación", callback_data="copy_trade"),
             InlineKeyboardButton("🧠 Inteligencia de ballenas", callback_data="smart_insights")],
            [InlineKeyboardButton("🛑 Detener copia", callback_data="stop_copying"),
             InlineKeyboardButton("📊 Mi portafolio", callback_data="my_stats")],
            [InlineKeyboardButton("⚙️ Configuración", callback_data="settings"),
             InlineKeyboardButton("💳 Plan PRO", callback_data="subscribe_pro")],
            [InlineKeyboardButton("🆓 Plan gratuito", callback_data="subscribe_free")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🤖 النسخ التلقائي", callback_data="auto_trading")],
            [InlineKeyboardButton("📈 نسخ صفقات الحيتان", callback_data="copy_trade"),
             InlineKeyboardButton("🧠 ذكاء الحيتان", callback_data="smart_insights")],
            [InlineKeyboardButton("🛑 إيقاف النسخ", callback_data="stop_copying"),
             InlineKeyboardButton("📊 محفظتي", callback_data="my_stats")],
            [InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
             InlineKeyboardButton("💳 اشتراك PRO", callback_data="subscribe_pro")],
            [InlineKeyboardButton("🆓 الخطة المجانية", callback_data="subscribe_free")]
        ]

    if user_id == ADMIN_ID and has_pending_payment:
        buttons.append([InlineKeyboardButton("✅ تأكيد الدفع يدويًا", callback_data="admin_confirm_payment")])

    return InlineKeyboardMarkup(buttons)
