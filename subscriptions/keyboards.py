from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import Session
from models.payment_requests import PaymentRequest

ADMIN_ID = 6672291052

def main_menu_keyboard(lang="ar", user_id=None):
    buttons = []

    if lang == "en":
        buttons = [
            [InlineKeyboardButton("📈 Copy Latest Trade", callback_data="copy_trade"),
             InlineKeyboardButton("💳 Subscription", callback_data="subscription_info")],
            [InlineKeyboardButton("📊 My Stats", callback_data="my_stats"),
             InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
            [InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")],
            [InlineKeyboardButton("ℹ️ Help", callback_data="how_it_works")]
        ]
    elif lang == "es":
        buttons = [
            [InlineKeyboardButton("📈 Copiar la última operación", callback_data="copy_trade"),
             InlineKeyboardButton("💳 Suscripción", callback_data="subscription_info")],
            [InlineKeyboardButton("📊 Mis estadísticas", callback_data="my_stats"),
             InlineKeyboardButton("⚙️ Configuración", callback_data="settings")],
            [InlineKeyboardButton("🤖 Trading automático", callback_data="auto_trading")],
            [InlineKeyboardButton("ℹ️ Ayuda", callback_data="how_it_works")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("📈 نسخ صفقات الحيتان", callback_data="copy_trade"),
             InlineKeyboardButton("💳 اشتراك", callback_data="subscription_info")],
            [InlineKeyboardButton("📊 إحصائياتي", callback_data="my_stats"),
             InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")],
            [InlineKeyboardButton("🤖 النسخ التلقائي", callback_data="auto_trading")],
            [InlineKeyboardButton("ℹ️ المساعدة", callback_data="how_it_works")]
        ]

    if user_id == ADMIN_ID:
        # زر تأكيد الدفع إذا كان في طلب معلّق
        session = Session()
        has_pending_payment = session.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first()
        session.close()
        if has_pending_payment:
            buttons.append([InlineKeyboardButton("✅ تأكيد الدفع يدويًا", callback_data="admin_confirm_payment")])

        # زر حذف سجل الصفقات دائمًا للأدمن
        buttons.append([InlineKeyboardButton("🧼 حذف سجل الصفقات", callback_data="admin_delete_trades")])

    return InlineKeyboardMarkup(buttons)
