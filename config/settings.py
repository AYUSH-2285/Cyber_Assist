import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = "sqlite:///../database/db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
