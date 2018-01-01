from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

# class SignUpForm(FlaskForm):
#     full_name = StringField('full_name', validators=[DataRequired()])
#     email = StringField('email', validators=[DataRequired()])
#     phone_number = IntegerField('phone_number', validators=[DataRequired()])

#######
'''
testing
'''
#######

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

def CheckNameLength(form, field):
  if len(field.data) < 4:
    raise ValidationError('Name must have more then 3 characters')

class ContactForm(FlaskForm):
    name = StringField('Full Name', [validators.DataRequired(), CheckNameLength])
    email = StringField('Email', [validators.DataRequired(),])
    phone_number = IntegerField('Phone Number:') # add validation
    message = TextAreaField('Your message:', [validators.DataRequired()])
    submit = SubmitField('SIGN UP')
