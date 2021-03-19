from flask import render_template, redirect, flash, url_for, session
from . import auth
from app.forms import LoginForm

@auth.route('/login', methods =['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con exito') #Manda un mensaje tipo alert

        return redirect(url_for('index'))

    return render_template('login.html', **context)
