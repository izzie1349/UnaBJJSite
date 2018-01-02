# from flask import Flask
import json
from app import app
from flask import render_template


# @app.route('/', methods=('GET', 'POST'))
# def home():
#     return render_template('landing_page.html')
#

###########
'''
test
'''
############

from flask import Flask, render_template, request, Response
from flask_mail import Mail, Message
from .forms import ContactForm
from .config.settings import(
    EMAIL,
    EMAIL_PASSWORD
)

app.secret_key = 'YourSuperSecreteKey'

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = EMAIL
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD

mail = Mail(app)
# from flask_bootstrap import Bootstrap as B
# B(app)

from flask import Flask, redirect, url_for, flash

@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm()

    if request.method == 'POST':
        # TODO backwards logic
        if form.validate() == True:
            return 'Please fill in all fields <p><a href="/contact">Try Again!!!</a></p>'
        else:
            msg = Message("Message from your visitor" + form.name.data,
                          sender=EMAIL,
                          recipients=['izzie1349+FRED@gmail.com',
                                      'izzie1349+ZOE@gmail.com',
                                      ])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.phone_number.data)
            mail.send(msg)
            return flash("Successfully  sent message!")
            # return redirect(url_for('landing_page') + '#thankYouHandHoldModal')
    elif request.method == 'GET':
        return render_template('landing_page.html', form=form)


@app.route('/ajax/contact', methods=("POST",))
def contact1():
    print "DATA: %s" %request.data
    return Response(json.dumps({
            'success': True
        }), mimetype=u'application/json')
