from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config

# Создаём экземпляр приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициализируем расширения
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импортируем остальные модули, чтобы зарегистрировать маршруты, команды и обработчики
from . import models
from . import views
from . import error_handlers
from . import cli_commands