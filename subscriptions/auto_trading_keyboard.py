from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def auto_trading_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("المبلغ لكل عملية شراء: -", callback_data="edit_buy_amount")],
        [InlineKeyboardButton("إجمالي مبلغ الشراء: -", callback_data="edit_total_amount")],
        [
            InlineKeyboardButton("رسوم الغاز للشراء: 0...", callback_data="edit_gas_buy"),
            InlineKeyboardButton("رسوم الغاز للبيع: 0...", callback_data="edit_gas_sell")
        ],
        [
            InlineKeyboardButton("نصيحة شراء MEV: 0...", callback_data="edit_mev_buy_tip"),
            InlineKeyboardButton("نصيحة بيع MEV: 0...", callback_data="edit_mev_sell_tip")
        ],
        [InlineKeyboardButton("🟠 مضاد MEV", callback_data="edit_mev_protection")],
        [
            InlineKeyboardButton("شراء الانزلاق: 20%", callback_data="edit_slippage_buy"),
            InlineKeyboardButton("بيع الانزلاق: 20%", callback_data="edit_slippage_sell")
        ],
        [InlineKeyboardButton("- شروط الشراء -", callback_data="none")],
        [
            InlineKeyboardButton(": -m :", callback_data="edit_buy_time_min"),
            InlineKeyboardButton(": -m :", callback_data="edit_buy_time_max")
        ],
        [
            InlineKeyboardButton("الحد الأدنى لرأس المال", callback_data="edit_min_cap"),
            InlineKeyboardButton("الحد الأقصى لرأس المال", callback_data="edit_max_cap")
        ],
        [
            InlineKeyboardButton("التغيير <=1m: 1%", callback_data="edit_change_1m"),
            InlineKeyboardButton("التغيير <=5m: 5%", callback_data="edit_change_5m")
        ],
        [
            InlineKeyboardButton("المعاملات <=1m: -", callback_data="edit_tx_1m"),
            InlineKeyboardButton("المعاملات <=5s: -", callback_data="edit_tx_5s")
        ],
        [
            InlineKeyboardButton("المعاملات التغيير <=1m: -%", callback_data="edit_change_tx_1m")
        ],
        [
            InlineKeyboardButton("كمية آخر 3 كتل: -", callback_data="edit_last_blocks_amount")
        ],
        [InlineKeyboardButton("- شروط البيع -", callback_data="none")]
    ])
