from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import Session
from models.payment_requests import PaymentRequest

ADMIN_ID = 6672291052

def main_menu_keyboard(user_id=None):
    session = Session()
    has_pending_payment = session.query(PaymentRequest).filter_by(user_id=user_id, status="pending").first()
    session.close()

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

    if user_id == ADMIN_ID and has_pending_payment:
        buttons.append([InlineKeyboardButton("✅ Confirm Payment", callback_data="admin_confirm_payment")])

    return InlineKeyboardMarkup(buttons)

def settings_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ])
