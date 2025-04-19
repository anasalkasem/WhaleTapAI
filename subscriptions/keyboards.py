from telegram import InlineKeyboardButton, InlineKeyboardMarkup

ADMIN_ID = 6672291052

def main_menu_keyboard(lang="ar", user_id=None):
    if lang == "en":
        buttons = [
            [
                InlineKeyboardButton("📈 Copy Whale Trades", callback_data="copy_trade"),
                InlineKeyboardButton("🤖 Auto-Trading", callback_data="auto_trading")
            ],
            [
                InlineKeyboardButton("Buy", callback_data="buy"),
                InlineKeyboardButton("Sell", callback_data="sell")
            ],
            [
                InlineKeyboardButton("Copy Trading 🛩️", callback_data="copy_trading"),
                InlineKeyboardButton("Manual Buy, Auto Sell", callback_data="manual_buy_auto_sell")
            ],
            [
                InlineKeyboardButton("Limit Orders", callback_data="limit_orders"),
                InlineKeyboardButton("⚙️ Settings", callback_data="settings")
            ],
            [
                InlineKeyboardButton("Wallet", callback_data="wallet"),
                InlineKeyboardButton("My Tokens", callback_data="my_tokens")
            ],
            [
                InlineKeyboardButton("💵 Smart Wallet", callback_data="smart_wallet"),
                InlineKeyboardButton("🖥️ Extension", callback_data="extension")
            ],
            [
                InlineKeyboardButton("📊 My Stats", callback_data="my_stats"),
                InlineKeyboardButton("💳 Subscription", callback_data="subscription_info")
            ],
            [
                InlineKeyboardButton("ℹ️ Help", callback_data="help"),
                InlineKeyboardButton("💰 Referrals", callback_data="referrals")
            ]
        ]
    elif lang == "es":
        buttons = [
            [
                InlineKeyboardButton("📈 Copiar Operaciones de Ballenas", callback_data="copy_trade"),
                InlineKeyboardButton("🤖 Comercio Automático", callback_data="auto_trading")
            ],
            [
                InlineKeyboardButton("Comprar", callback_data="buy"),
                InlineKeyboardButton("Vender", callback_data="sell")
            ],
            [
                InlineKeyboardButton("Copy Trading 🛩️", callback_data="copy_trading"),
                InlineKeyboardButton("Compra Manual, Venta Automática", callback_data="manual_buy_auto_sell")
            ],
            [
                InlineKeyboardButton("Órdenes Limitadas", callback_data="limit_orders"),
                InlineKeyboardButton("⚙️ Configuración", callback_data="settings")
            ],
            [
                InlineKeyboardButton("Cartera", callback_data="wallet"),
                InlineKeyboardButton("Mis Tokens", callback_data="my_tokens")
            ],
            [
                InlineKeyboardButton("💵 Cartera Inteligente", callback_data="smart_wallet"),
                InlineKeyboardButton("🖥️ Extensión", callback_data="extension")
            ],
            [
                InlineKeyboardButton("📊 Mis Estadísticas", callback_data="my_stats"),
                InlineKeyboardButton("💳 Suscripción", callback_data="subscription_info")
            ],
            [
                InlineKeyboardButton("ℹ️ Ayuda", callback_data="help"),
                InlineKeyboardButton("💰 Referencias", callback_data="referrals")
            ]
        ]
    else:
        buttons = [
            [
                InlineKeyboardButton("📈 نسخ صفقات الحيتان", callback_data="copy_trade"),
                InlineKeyboardButton("🤖 التداول التلقائي", callback_data="auto_trading")
            ],
            [
                InlineKeyboardButton("شراء", callback_data="buy"),
                InlineKeyboardButton("بيع", callback_data="sell")
            ],
            [
                InlineKeyboardButton("نسخ التداول 🛩️", callback_data="copy_trading"),
                InlineKeyboardButton("شراء يدوي، بيع تلقائي", callback_data="manual_buy_auto_sell")
            ],
            [
                InlineKeyboardButton("أوامر الحد", callback_data="limit_orders"),
                InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")
            ],
            [
                InlineKeyboardButton("المحفظة", callback_data="wallet"),
                InlineKeyboardButton("العملات لدي", callback_data="my_tokens")
            ],
            [
                InlineKeyboardButton("💵 المحفظة الذكية", callback_data="smart_wallet"),
                InlineKeyboardButton("🖥️ امتداد", callback_data="extension")
            ],
            [
                InlineKeyboardButton("📊 إحصائياتي", callback_data="my_stats"),
                InlineKeyboardButton("💳 اشتراك", callback_data="subscription_info")
            ],
            [
                InlineKeyboardButton("ℹ️ المساعدة", callback_data="help"),
                InlineKeyboardButton("💰 الإحالات", callback_data="referrals")
            ]
        ]

    if user_id == ADMIN_ID:
        buttons.append([InlineKeyboardButton("🧼 حذف سجل الصفقات", callback_data="admin_delete_trades")])

    return InlineKeyboardMarkup(buttons)
