import os
import asyncio
import nest_asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from db_utils import init_db

# ... (استيراد كل الهاندلرز اللي عندك)

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_DOMAIN}{WEBHOOK_PATH}"

async def run():
    init_db()

    application = Application.builder().token(TOKEN).build()

    # handlers
    application.add_handler(CommandHandler("start", handle_main_menu))
    application.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))
    # ... باقي الهاندلرز

    await application.bot.delete_webhook()

    await application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(run())
