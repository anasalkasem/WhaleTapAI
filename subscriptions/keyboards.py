from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📈 نسخ صفقات الحيتان", callback_data="copy_trade"),
            InlineKeyboardButton("💳 اشتراك", callback_data="subscription_info")
        ],
        [
            InlineKeyboardButton("📊 إحصائياتي", callback_data="my_stats"),
            InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")
        ],
        [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")]
    ])

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
    else:  # Arabic
        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⭐ اشتراك PRO - 20$", callback_data="subscribe_pro"),
                InlineKeyboardButton("🆓 نسخة تجريبية", callback_data="subscribe_free")
            ],
            [InlineKeyboardButton("📋 كيف يعمل البوت؟", callback_data="how_it_works")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ])

def crypto_payment_keyboard(plan: str, lang="ar"):
    if lang == "en":
        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("💠 Pay with SOL", callback_data=f"pay_sol_{plan}"),
                InlineKeyboardButton("💎 Pay with USDT", callback_data=f"pay_usdt_{plan}")
            ],
            [InlineKeyboardButton("↩️ Back", callback_data="back_to_plans")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ])
    elif lang == "es":
        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("💠 Pagar con SOL", callback_data=f"pay_sol_{plan}"),
                InlineKeyboardButton("💎 Pagar con USDT", callback_data=f"pay_usdt_{plan}")
            ],
            [InlineKeyboardButton("↩️ Atrás", callback_data="back_to_plans")],
            [InlineKeyboardButton("🏠 Menú principal", callback_data="main_menu")]
        ])
    else:  # Arabic
        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("💠 دفع بـ SOL", callback_data=f"pay_sol_{plan}"),
                InlineKeyboardButton("💎 دفع بـ USDT", callback_data=f"pay_usdt_{plan}")
            ],
            [InlineKeyboardButton("↩️ رجوع", callback_data="back_to_plans")],
            [InlineKeyboardButton("🏠 الرئيسية", callback_data="main_menu")]
        ])
