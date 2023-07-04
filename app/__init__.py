from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager


from app.db import db
from app.models import Employee, Position, Division, Job, User
from app.views import bp
from app.templates.config import Config
from app.auth import auth


app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:5051PiDoR5051@localhost:5432/lb5_6"

db.init_app(app)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(bp)
app.register_blueprint(auth)
