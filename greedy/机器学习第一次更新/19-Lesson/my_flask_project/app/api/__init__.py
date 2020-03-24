__author__ = "zhou"
__date__ = "2019-06-06 21:43"

from flask import Blueprint
api = Blueprint('api', __name__)

from app.api import goods
from app.api import user







