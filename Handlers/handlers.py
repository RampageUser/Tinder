from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Text


@dp.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(text='This bot was making for dating')