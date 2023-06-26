from flask import Flask
from flask_migrate import Migrate


from .db import db
from .models import Employee, Position, Division, Job
from .views import bp
from templates.config import Config


app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:5051PiDoR5051@localhost:5432/lb5_6"
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(bp)
