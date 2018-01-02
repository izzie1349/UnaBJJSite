#!flask/bin/python
import os

from app import app
from flask_bootstrap import Bootstrap

Bootstrap(app)
app.run(host='0.0.0.0', port=os.getenv('PORT'))
