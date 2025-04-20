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
