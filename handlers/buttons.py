from aiogram import Router, types
from aiogram.types import CallbackQuery
from keyboards.inline import get_main_keyboard

router = Router()

@router.callback_query()
async def handle_buttons(callback: CallbackQuery):
    if callback.data == "weather":
        await callback.message.answer("🌦 Сейчас проверю погоду...")
    elif callback.data == "donate":
        await callback.message.answer("💰 Поддержите нас по ссылке: https://donate.com")
    
    await callback.answer()
