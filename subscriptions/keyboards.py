from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import SessionLocal
from models.user_subscriptions import UserSubscription

ADMIN_IDS = [6672291052]

def user_has_pro(user_id: int) -> bool:
    db = SessionLocal()
    result = db.query(UserSubscription).filter_by(user_id=user_id, plan_type="pro").first()
    db.close()
    return result is not None

def has_pending_payment_request(user_id: int) -> bool:
    db = SessionLocal()
    from models.payment_requests import PaymentRequest
    result = db.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first()
    db.close()
    return result is not None

def main_menu_keyboard(user_id):
    keyboard = [
        [
            InlineKeyboardButton("🛒 Trading", callback_data="trading"),
            InlineKeyboardButton("🤖 AI Trading", callback_data="auto_trading"),
            InlineKeyboardButton("💼 Wallet", callback_data="wallet"),
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
            InlineKeyboardButton("📊 Portfolio", callback_data="my_stats"),
        ],
        [
            InlineKeyboardButton("🧠 Smart Insights", callback_data="smart_insights"),
            InlineKeyboardButton("🛑 Stop Copying", callback_data="stop_copying"),
        ]
    ]

    # زر الاشتراك حسب حالة المستخدم
    if user_has_pro(user_id):
        keyboard.append([
            InlineKeyboardButton("⭐ You are PRO", callback_data="already_pro")
        ])
    else:
        keyboard.append([
            InlineKeyboardButton("💳 Subscribe PRO", callback_data="subscribe_pro"),
            InlineKeyboardButton("🆓 Free Plan", callback_data="subscribe_free"),
        ])

    # زر تأكيد الدفع يظهر فقط إذا كان المستخدم أدمن ويوجد طلب معلق
    if user_id in ADMIN_IDS and has_pending_payment_request(user_id):
        keyboard.append([
            InlineKeyboardButton("✅ Confirm Payment", callback_data="admin_confirm_payment")
        ])

    return InlineKeyboardMarkup(keyboard)
