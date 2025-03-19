import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [123456789, 987654321]
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///bot.db")