from aiogram import Router, types
from aiogram.filters import Command
from keyboards.inline import get_main_keyboard

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Выбери действие:",
        reply_markup=get_main_keyboard()
    )
