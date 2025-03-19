from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💡 Узнать погоду", callback_data="weather")],
        [InlineKeyboardButton(text="💰 Пойти искать в гугле", url="https://www.google.com")],
    ])
