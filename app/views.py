import flask,flask_mail

from . import app,mail


@app.route("/", methods=['GET','POST'])
def index():
    if flask.request.method=="POST":

        firstname=flask.request.form.get('firstname')
        lastname=flask.request.form.get('lastname')
        email=flask.request.form.get('email')
        countryCode=flask.request.form.get('countryCode')
        phone=flask.request.form.get('phone')
        job=flask.request.form.get('job')
        company=flask.request.form.get('company')
        message=flask.request.form.get('message')

        msg=flask_mail.Message(subject="Hit for Steinherz Media", body="{} {}, {}, from {} company sent you a message.\nThe message is: {}.\nThe return e-mail address is: {}\nThe phone number is: country code ({}) {}".format(firstname,lastname,job, company, message,email,countryCode,phone) ,
                  sender=('steinherzmedia@gmail.com'),
                  recipients=['steinherzmedia@gmail.com'])
        mail.send(msg)
        flask.flash("Your message has been sent successfully. Steinherz Media will contact you shortly.")
        return flask.redirect(flask.url_for('index'))
    return flask.render_template("index.html")

