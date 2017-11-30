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
###########
'''
test
'''
############

from flask import Flask, render_template, request
from flask_mail import Mail, Message
from forms import ContactForm


app.secret_key = 'YourSuperSecreteKey'

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'damiank1349@gmail.com'
app.config['MAIL_PASSWORD'] = 'theexorcist357'

mail = Mail(app)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            return 'Please fill in all fields <p><a href="/contact">Try Again!!!</a></p>'
        else:
            msg = Message("Message from your visitor" + form.name.data,
                          sender='YourUser@NameHere',
                          recipients=['yourRecieve@mail.com', 'someOther@mail.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return "Successfully  sent message!"
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
