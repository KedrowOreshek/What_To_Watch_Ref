import os
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные из .env


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
