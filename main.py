import os
import uvicorn
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from fastapi import FastAPI, Request
from telegram import Update

# استيراد كل الدوال
from subscriptions.main_menu_handler import handle_main_menu, handle_subscription_info, handle_back_to_plans
from subscriptions.copy_trade_handler import handle_copy_trade
from subscriptions.auto_trading_handlers import handle_auto_trading, handle_stop_copying
from subscriptions.stats_handler import handle_my_stats
from subscriptions.settings_handler import handle_settings
from subscriptions.insights_handler import handle_smart_insights
from utils.delete_table_whale_trades_v2 import handle_delete_trades
from admin.confirm_payment_handler import handle_confirm_payment

# إعداد المتغيرات
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.environ.get("PORT", 8000))

# FastAPI
app = FastAPI()

application = Application.builder().token(TOKEN).build()

# Endpoint للويب هوك
@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, application.bot)
    await application.update_queue.put(update)
    return {"status": "ok"}

# عند بداية التشغيل
@app.on_event("startup")
async def on_startup():
    await application.bot.set_webhook(url=WEBHOOK_URL)
    print("✅ Webhook has been set.")

# Handlers
application.add_handler(CommandHandler("start", handle_main_menu))
application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
application.add_handler(CallbackQueryHandler(handle_subscription_info, pattern="^subscription_info$"))
application.add_handler(CallbackQueryHandler(handle_back_to_plans, pattern="^back_to_plans$"))
application.add_handler(CallbackQueryHandler(handle_copy_trade, pattern="^copy_trade$"))
application.add_handler(CallbackQueryHandler(handle_auto_trading, pattern="^auto_trading$"))
application.add_handler(CallbackQueryHandler(handle_stop_copying, pattern="^stop_copying$"))
application.add_handler(CallbackQueryHandler(handle_my_stats, pattern="^my_stats$"))
application.add_handler(CallbackQueryHandler(handle_settings, pattern="^settings$"))
application.add_handler(CallbackQueryHandler(handle_smart_insights, pattern="^smart_insights$"))
application.add_handler(CallbackQueryHandler(handle_delete_trades, pattern="^admin_delete_trades$"))
application.add_handler(CallbackQueryHandler(handle_confirm_payment, pattern="^admin_confirm_payment$"))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
