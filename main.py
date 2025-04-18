from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import asyncio
import nest_asyncio
import logging

from handlers.main_menu import handle_main_menu
from handlers.copy_trade import handle_copy_trade

API_TOKEN = "YOUR_BOT_TOKEN"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://your-app-url.railway.app{WEBHOOK_PATH}"

nest_asyncio.apply()
logging.basicConfig(level=logging.INFO)

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(WEBHOOK_URL)

def create_app():
    session = AiohttpSession()
    bot = Bot(token=API_TOKEN, session=session, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.register(handle_main_menu, commands={"start"})
    dp.message.register(handle_copy_trade, lambda msg: msg.text == "📥 Copy Latest Trade")

    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    app.on_startup.append(lambda app: on_startup(bot))
    return app

app = create_app()

if __name__ == "__main__":
    web.run_app(app, port=int(os.getenv("PORT", 8000)))