from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import Session
from models.payment_requests import PaymentRequest

ADMIN_ID = 6672291052

def main_menu_keyboard(lang="ar", user_id=None):
    session = Session()
    has_pending_payment = session.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first()
    session.close()

    if lang == "en":
        buttons = [
            [InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")],
            [InlineKeyboardButton("📈 Copy Latest Trade", callback_data="copy_trade"),
             InlineKeyboardButton("🧠 Smart Whale Insights", callback_data="smart_insights")],
            [InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
             InlineKeyboardButton("📊 My Portfolio", callback_data="my_stats")],
            [InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
             InlineKeyboardButton("💳 Upgrade to PRO", callback_data="subscription_info")],
            [InlineKeyboardButton("🆓 Free Plan", callback_data="subscribe_free")]
        ]
    elif lang == "es":
        buttons = [
            [InlineKeyboardButton("🤖 Trading automático", callback_data="auto_trading")],
            [InlineKeyboardButton("📈 Copiar última operación", callback_data="copy_trade"),
             InlineKeyboardButton("🧠 Análisis de ballenas inteligentes", callback_data="smart_insights")],
            [InlineKeyboardButton("🛑 Detener copia", callback_data="stop_copying"),
             InlineKeyboardButton("📊 Mi portafolio", callback_data="my_stats")],
            [InlineKeyboardButton("⚙️ Configuración", callback_data="settings"),
             InlineKeyboardButton("💳 Actualizar a PRO", callback_data="subscription_info")],
            [InlineKeyboardButton("🆓 Plan gratuito", callback_data="subscribe_free")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🤖 النسخ التلقائي", callback_data="auto_trading")],
            [InlineKeyboardButton("📈 نسخ أحدث صفقة", callback_data="copy_trade"),
             InlineKeyboardButton("🧠 تحليلات الحيتان الذكية", callback_data="smart_insights")],
            [InlineKeyboardButton("🛑 إيقاف النسخ", callback_data="stop_copying"),
             InlineKeyboardButton("📊 محفظتي", callback_data="my_stats")],
            [InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
             InlineKeyboardButton("💳 ترقية إلى PRO", callback_data="subscription_info")],
            [InlineKeyboardButton("🆓 خطة مجانية", callback_data="subscribe_free")]
        ]

    # إضافة زر تأكيد الدفع يدويًا فقط إذا كان المستخدم هو الأدمن ولديه طلب دفع معلق
    if user_id == ADMIN_ID and has_pending_payment:
        buttons.append([InlineKeyboardButton("✅ تأكيد الدفع يدويًا", callback_data="admin_confirm_payment")])

    return InlineKeyboardMarkup(buttons)
