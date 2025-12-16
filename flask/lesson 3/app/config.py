import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "T-73V37.")
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SQLACHEMY_TRACK_MODIFICATIONS = False