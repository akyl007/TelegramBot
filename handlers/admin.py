from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_IDS

router = Router()

@router.message(Command("admin"))
async def admin_handler(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ У вас нет доступа к этой команде.")
        return
    
    await message.answer("🔧 Панель администратора:\n\n"
                         "/stats - Статистика пользователей\n"
                         "/broadcast <текст> - Рассылка")
