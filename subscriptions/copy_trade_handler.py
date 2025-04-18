from aiogram.types import Message

async def handle_copy_trade(message: Message):
    await message.answer("✅ Trade copied successfully!
We'll notify you when similar trades happen.")
