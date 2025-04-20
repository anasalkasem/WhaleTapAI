from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from db_utils import get_user_language

# === لوحة إعدادات التداول التلقائي ===
def auto_trading_keyboard(lang="ar"):
    if lang == "en":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("Buy Amount Per Trade: -", callback_data="edit_buy_amount")],
            [InlineKeyboardButton("Total Buy Amount: -", callback_data="edit_total_amount")],
            [
                InlineKeyboardButton("Gas (Buy): 0...", callback_data="edit_gas_buy"),
                InlineKeyboardButton("Gas (Sell): 0...", callback_data="edit_gas_sell")
            ],
            [
                InlineKeyboardButton("MEV Tip (Buy): 0...", callback_data="edit_mev_buy_tip"),
                InlineKeyboardButton("MEV Tip (Sell): 0...", callback_data="edit_mev_sell_tip")
            ],
            [InlineKeyboardButton("🟠 MEV Protection", callback_data="edit_mev_protection")],
            [
                InlineKeyboardButton("Slippage Buy: 20%", callback_data="edit_slippage_buy"),
                InlineKeyboardButton("Slippage Sell: 20%", callback_data="edit_slippage_sell")
            ],
            [InlineKeyboardButton("- Buy Conditions -", callback_data="none")],
            [
                InlineKeyboardButton("Min Buy Time: -m", callback_data="edit_buy_time_min"),
                InlineKeyboardButton("Max Buy Time: -m", callback_data="edit_buy_time_max")
            ],
            [
                InlineKeyboardButton("Min Cap", callback_data="edit_min_cap"),
                InlineKeyboardButton("Max Cap", callback_data="edit_max_cap")
            ],
            [
                InlineKeyboardButton("Change <=1m: 1%", callback_data="edit_change_1m"),
                InlineKeyboardButton("Change <=5m: 5%", callback_data="edit_change_5m")
            ],
            [
                InlineKeyboardButton("Txs <=1m: -", callback_data="edit_tx_1m"),
                InlineKeyboardButton("Txs <=5s: -", callback_data="edit_tx_5s")
            ],
            [
                InlineKeyboardButton("Change Txs <=1m: -%", callback_data="edit_change_tx_1m")
            ],
            [
                InlineKeyboardButton("Last 3 Blocks Amount: -", callback_data="edit_last_blocks_amount")
            ],
            [InlineKeyboardButton("- Sell Conditions -", callback_data="none")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ])
    
    elif lang == "es":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("Monto por compra: -", callback_data="edit_buy_amount")],
            [InlineKeyboardButton("Monto total de compra: -", callback_data="edit_total_amount")],
            [
                InlineKeyboardButton("Gas (compra): 0...", callback_data="edit_gas_buy"),
                InlineKeyboardButton("Gas (venta): 0...", callback_data="edit_gas_sell")
            ],
            [
                InlineKeyboardButton("MEV Tip (compra): 0...", callback_data="edit_mev_buy_tip"),
                InlineKeyboardButton("MEV Tip (venta): 0...", callback_data="edit_mev_sell_tip")
            ],
            [InlineKeyboardButton("🟠 Protección MEV", callback_data="edit_mev_protection")],
            [
                InlineKeyboardButton("Slippage compra: 20%", callback_data="edit_slippage_buy"),
                InlineKeyboardButton("Slippage venta: 20%", callback_data="edit_slippage_sell")
            ],
            [InlineKeyboardButton("- Condiciones de compra -", callback_data="none")],
            [
                InlineKeyboardButton("Tiempo mínimo: -m", callback_data="edit_buy_time_min"),
                InlineKeyboardButton("Tiempo máximo: -m", callback_data="edit_buy_time_max")
            ],
            [
                InlineKeyboardButton("Capital mínimo", callback_data="edit_min_cap"),
                InlineKeyboardButton("Capital máximo", callback_data="edit_max_cap")
            ],
            [
                InlineKeyboardButton("Cambio <=1m: 1%", callback_data="edit_change_1m"),
                InlineKeyboardButton("Cambio <=5m: 5%", callback_data="edit_change_5m")
            ],
            [
                InlineKeyboardButton("Txs <=1m: -", callback_data="edit_tx_1m"),
                InlineKeyboardButton("Txs <=5s: -", callback_data="edit_tx_5s")
            ],
            [
                InlineKeyboardButton("Cambio en txs <=1m: -%", callback_data="edit_change_tx_1m")
            ],
            [
                InlineKeyboardButton("Monto últimos 3 bloques: -", callback_data="edit_last_blocks_amount")
            ],
            [InlineKeyboardButton("- Condiciones de venta -", callback_data="none")],
            [InlineKeyboardButton("🏠 Menú principal", callback_data="main_menu")]
        ])
    
    else:
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
            [InlineKeyboardButton("- شروط البيع -", callback_data="none")],
            [InlineKeyboardButton("🏠 العودة إلى القائمة الرئيسية", callback_data="main_menu")]
        ])

# === دالة عرض واجهة النسخ التلقائي ===
async def handle_auto_trading(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id)
    keyboard = auto_trading_keyboard(lang=user_lang)

    text = {
        "ar": "⚙️ إعدادات التداول التلقائي:\nقم بتعديل المعايير أدناه لإنشاء أو تخصيص نمط التداول التلقائي الخاص بك.",
        "en": "⚙️ Auto-Trading Settings:\nAdjust the parameters below to create or customize your strategy.",
        "es": "⚙️ Configuración de trading automático:\nAjusta los parámetros abajo para tu estrategia."
    }.get(user_lang, "⚙️ Auto-Trading Settings")

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=keyboard
    )
