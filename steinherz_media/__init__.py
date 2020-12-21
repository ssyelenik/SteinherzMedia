import os
import flask,flask_mail


app=flask.Flask(__name__)

basedir=os.path.dirname(__file__)
app.config['SECRET_KEY']='mnisghh12345'
app.config['MAIL_SERVER']     = "smtp.gmail.com"
app.config['MAIL_PORT']       = 587
app.config['MAIL_USE_TLS']    = True
app.config['MAIL_USE_SSL']    = False
app.config['MAIL_USERNAME']   = 'steinherzmedia'
app.config['MAIL_PASSWORD']   = '1234abcd!'
mail=flask_mail.Mail(app)

from . import views