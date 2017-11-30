from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class SignUpForm(Form):
    full_name = StringField('full_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    phone_number = IntegerField('phone_number', validators=[DataRequired()])
