from aiogram.types import Message
from subscriptions.keyboards import main_menu_keyboard

async def handle_main_menu(message: Message):
    await message.answer("Welcome to WhaleTap! Choose an option:", reply_markup=main_menu_keyboard())