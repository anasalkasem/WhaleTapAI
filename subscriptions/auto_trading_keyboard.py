from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def auto_trading_keyboard():
    keyboard = [
        [InlineKeyboardButton("اختر قالب 🟠", callback_data='choose_template')],
        [InlineKeyboardButton("المبلغ لكل عملية شراء: -", callback_data='buy_amount_each')],
        [InlineKeyboardButton("إجمالي مبلغ الشراء: -", callback_data='total_buy_amount')],
        [
            InlineKeyboardButton("رسوم الغاز للبيع: 0...", callback_data='sell_gas_fee'),
            InlineKeyboardButton("رسوم الغاز للشراء: 0...", callback_data='buy_gas_fee')
        ],
        [
            InlineKeyboardButton("نصيحة بيع MEV: 0...", callback_data='sell_mev'),
            InlineKeyboardButton("نصيحة شراء MEV: ...", callback_data='buy_mev')
        ],
        [InlineKeyboardButton("🟠 مضاد MEV", callback_data='mev_protection')],
        [
            InlineKeyboardButton("بيع الانزلاق: 20%", callback_data='sell_slippage'),
            InlineKeyboardButton("شراء الانزلاق: 20%", callback_data='buy_slippage')
        ],
        [InlineKeyboardButton("- شروط الشراء -", callback_data='buy_conditions')],
        [
            InlineKeyboardButton("الحد الأقصى لرأس المال: -", callback_data='max_cap'),
            InlineKeyboardButton("الحد الأدنى لرأس المال: -", callback_data='min_cap')
        ],
        [
            InlineKeyboardButton("5m: ≥-% التغيير", callback_data='change_5m'),
            InlineKeyboardButton("1m: ≥-% التغيير", callback_data='change_1m')
        ],
        [InlineKeyboardButton("5m: ≥-% التغيير/الحد الأدنى", callback_data='min_change_5m')],
        [
            InlineKeyboardButton("5s المعاملات: ≥-", callback_data='txs_5s'),
            InlineKeyboardButton("1m المعاملات: ≥-", callback_data='txs_1m')
        ],
        [InlineKeyboardButton("1m المعاملات التغيير: ≥-%", callback_data='txs_change_1m')],
        [InlineKeyboardButton("كمية آخر 3 كتل: -", callback_data='last_blocks_volume')],
        [InlineKeyboardButton("- شروط البيع -", callback_data='sell_conditions')],
        [
            InlineKeyboardButton("➕ إضافة", callback_data='add_autotrade'),
            InlineKeyboardButton("إنشاء ✅", callback_data='create_autotrade')
        ],
        [InlineKeyboardButton("← العودة", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)
