from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import InputRequired, Optional, Length, Email


class CustomerForm(FlaskForm):
    phone = StringField('Телефон', validators=[InputRequired(), Length(min=5, max=20)])
    email = StringField('E-Mail', validators=[Optional(), Email(), Length(min=3, max=100)])
    name = StringField('Имя', validators=[Optional(), Length(max=255)])
