from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import Session
from models.payment_requests import PaymentRequest

ADMIN_ID = 6672291052

# القائمة الرئيسية
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
        session = Session()
        has_pending_payment = session.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first()
        session.close()
        if has_pending_payment:
            buttons.append([InlineKeyboardButton("✅ تأكيد الدفع يدويًا", callback_data="admin_confirm_payment")])

    return InlineKeyboardMarkup(buttons)

# خطط الاشتراك
def plans_keyboard(lang="ar"):
    if lang == "en":
        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⭐ PRO Plan - $20", callback_data="subscribe_pro"),
                InlineKeyboardButton("🆓 Free Trial", callback_data="subscribe_free")
            ],
            [InlineKeyboardButton("📋 How does the bot work?", callback_data="how_it_works")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ])
    elif lang == "es":
        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⭐ Plan PRO - $20", callback_data="subscribe_pro"),
                InlineKeyboardButton("🆓 Prueba gratuita", callback_data="subscribe_free")
            ],
            [InlineKeyboardButton("📋 ¿Cómo funciona el bot?", callback_data="how_it_works")],
            [InlineKeyboardButton("🏠 Menú principal", callback_data="main_menu")]
        ])
    else:
        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro"),
                InlineKeyboardButton("🆓 نسخة تجريبية", callback_data="subscribe_free")
            ],
            [InlineKeyboardButton("📋 كيف يعمل البوت؟", callback_data="how_it_works")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ])
