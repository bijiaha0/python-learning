__author__ = "zhou"
__date__ = "2019-06-06 22:16"

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()

class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False, unique=True)



