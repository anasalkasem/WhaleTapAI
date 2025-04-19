from telegram import InlineKeyboardButton, InlineKeyboardMarkup

ADMIN_ID = 6672291052

def main_menu_keyboard(lang="ar", user_id=None):
    buttons = []

    if lang == "en":
        buttons = [
            [
                InlineKeyboardButton("📈 Copy Latest Trade", callback_data="copy_trade"),
                InlineKeyboardButton("💳 Subscription", callback_data="subscription_info")
            ],
            [
                InlineKeyboardButton("📊 My Stats", callback_data="my_stats"),
                InlineKeyboardButton("⚙️ Settings", callback_data="settings")
            ],
            [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
        ]
    elif lang == "es":
        buttons = [
            [
                InlineKeyboardButton("📈 Copiar la última operación", callback_data="copy_trade"),
                InlineKeyboardButton("💳 Suscripción", callback_data="subscription_info")
            ],
            [
                InlineKeyboardButton("📊 Mis estadísticas", callback_data="my_stats"),
                InlineKeyboardButton("⚙️ Configuración", callback_data="settings")
            ],
            [InlineKeyboardButton("ℹ️ Ayuda", callback_data="help")]
        ]
    else:
        buttons = [
            [
                InlineKeyboardButton("📈 نسخ صفقات الحيتان", callback_data="copy_trade"),
                InlineKeyboardButton("💳 اشتراك", callback_data="subscription_info")
            ],
            [
                InlineKeyboardButton("📊 إحصائياتي", callback_data="my_stats"),
                InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")
            ],
            [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")]
        ]

    # إضافة زر الأدمن
    if user_id == ADMIN_ID:
        buttons.append([InlineKeyboardButton("🧼 حذف سجل الصفقات", callback_data="admin_delete_trades")])

    return InlineKeyboardMarkup(buttons)
