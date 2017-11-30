# from flask import Flask
from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('landing_page.html')

@app.route('/signup')
def sign_up():
    return render_template('landing_page.html',
                            form=form)
