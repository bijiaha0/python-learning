
__author__ = "zhou"
__date__ = "2019-06-06 22:02"

from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length


class UserForm(Form):
    username = StringField(validators=[DataRequired(), Length(min=5, max=10)])





