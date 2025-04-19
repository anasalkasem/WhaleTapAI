from telegram import InlineKeyboardButton, InlineKeyboardMarkup

ADMIN_ID = 6672291052

# القائمة الرئيسية
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

    # زر حذف الصفقات فقط للأدمن
    if user_id == ADMIN_ID:
        buttons.append([InlineKeyboardButton("🧼 حذف سجل الصفقات", callback_data="admin_delete_trades")])

    return InlineKeyboardMarkup(buttons)

# لوحة خطط الاشتراك
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

# لوحة الدفع بالعملات الرقمية
def crypto_payment_keyboard(plan: str, lang="ar"):
    if lang == "en":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("💠 Pay with SOL", callback_data=f"pay_sol_{plan}")],
            [InlineKeyboardButton("↩️ Back to Plans", callback_data="back_to_plans")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ])
    elif lang == "es":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("💠 Pagar con SOL", callback_data=f"pay_sol_{plan}")],
            [InlineKeyboardButton("↩️ Volver a planes", callback_data="back_to_plans")],
            [InlineKeyboardButton("🏠 Menú principal", callback_data="main_menu")]
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("💠 دفع بـ SOL", callback_data=f"pay_sol_{plan}")],
            [InlineKeyboardButton("↩️ رجوع إلى الخطط", callback_data="back_to_plans")],
            [InlineKeyboardButton("🏠 الرئيسية", callback_data="main_menu")]
        ])

# لوحة الإعدادات
def settings_keyboard(lang="ar"):
    if lang == "en":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🌐 Change Language", callback_data="change_language")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ])
    elif lang == "es":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🌐 Cambiar idioma", callback_data="change_language")],
            [InlineKeyboardButton("🏠 Menú principal", callback_data="main_menu")]
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🌐 تغيير اللغة", callback_data="change_language")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ])

# لوحة اختيار اللغة
def language_selection_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar"),
            InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
            InlineKeyboardButton("🇪🇸 Español", callback_data="lang_es"),
        ],
        [InlineKeyboardButton("↩️ رجوع", callback_data="settings")]
    ])
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def auto_trading_keyboard():
    keyboard = [
        [InlineKeyboardButton("المبلغ لكل عملية شراء: -", callback_data="amount_per_trade")],
        [InlineKeyboardButton("إجمالي مبلغ الشراء: -", callback_data="total_purchase_amount")],
        [
            InlineKeyboardButton("رسوم الغاز للشراء: 0...", callback_data="gas_fee_buy"),
            InlineKeyboardButton("رسوم الغاز للبيع: 0...", callback_data="gas_fee_sell")
        ],
        [
            InlineKeyboardButton("نصيحة شراء MEV: ...", callback_data="mev_buy"),
            InlineKeyboardButton("نصيحة بيع MEV: 0...", callback_data="mev_sell")
        ],
        [InlineKeyboardButton("🟠 مضاد MEV", callback_data="mev_protection")],
        [
            InlineKeyboardButton("شراء الانزلاق: %20", callback_data="slippage_buy"),
            InlineKeyboardButton("بيع الانزلاق: %20", callback_data="slippage_sell")
        ],
        [InlineKeyboardButton("-شروط الشراء-", callback_data="buy_conditions")],
        [
            InlineKeyboardButton("-m: :", callback_data="min_condition_m"),
            InlineKeyboardButton("-m: :", callback_data="max_condition_m")
        ],
        [
            InlineKeyboardButton("الحد الأدنى لرأس المال", callback_data="min_cap"),
            InlineKeyboardButton("الحد الأقصى لرأس المال", callback_data="max_cap")
        ],
        [
            InlineKeyboardButton("التغيير: ≥-% 1m", callback_data="change_1m"),
            InlineKeyboardButton("التغيير: ≥-% 5m", callback_data="change_5m")
        ],
        [InlineKeyboardButton("التغيير/الحد الأدنى 5m: ≥-%", callback_data="change_min_5m")],
        [
            InlineKeyboardButton("المعاملات 5s: ≥-", callback_data="tx_5s"),
            InlineKeyboardButton("المعاملات 1m: ≥-", callback_data="tx_1m")
        ],
        [InlineKeyboardButton("المعاملات التغيير 1m: ≥-%", callback_data="tx_change_1m")],
        [InlineKeyboardButton("كمية آخر 3 كتل: -", callback_data="last_blocks_volume")],
        [InlineKeyboardButton("-شروط البيع-", callback_data="sell_conditions")],
        [
            InlineKeyboardButton("إضافة", callback_data="auto_add"),
            InlineKeyboardButton("إنشاء", callback_data="auto_create")
        ],
        [InlineKeyboardButton("← العودة", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)
