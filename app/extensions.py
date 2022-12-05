from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import loginManager

db =SQLAlchemy()
migrate = Migrate()

login_manager = loginManager()
login_manager.login_view = 'auth.login'