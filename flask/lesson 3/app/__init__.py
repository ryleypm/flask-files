from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import routes, models