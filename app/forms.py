from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class SignUpForm(Form):
    full_name = StringField('full_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    phone_number = IntegerField('phone_number', validators=[DataRequired()])

#######
'''
testing
'''
#######

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

def CheckNameLength(form, field):
  if len(field.data) < 4:
    raise ValidationError('Name must have more then 3 characters')

class ContactForm(Form):
    name = StringField('Your Name:', [validators.DataRequired(), CheckNameLength])
    email = StringField('Your e-mail address:', [validators.DataRequired(), validators.Email('your@email.com')])
    message = TextAreaField('Your message:', [validators.DataRequired()])
    submit = SubmitField('Send Message')
