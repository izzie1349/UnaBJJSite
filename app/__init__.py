'''
We need to tell Flask to read our config file and use it. We can do this
right after the Flask app object is created:
'''
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
