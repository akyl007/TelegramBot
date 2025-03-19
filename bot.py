import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import start, buttons, admin

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Регистрируем обработчики
dp.include_router(start.router)
dp.include_router(buttons.router)
dp.include_router(admin.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
