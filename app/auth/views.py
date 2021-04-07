from flask import render_template, redirect, flash, url_for, session
from flask_login import login_user, login_required, logout_user
from . import auth
from app.forms import LoginForm
from app.firestore_service import get_user, user_put
from app.models import UserData, UserModel
from werkzeug.security import generate_password_hash, check_password_hash #libreria de seguridad

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))


@auth.route('/login', methods =['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            if check_password_hash(password_from_db, password):
                user_data = UserData(username,password)
                user = UserModel(user_data)

                login_user(user) #Metodo propio del login de flask

                flash('Bienvenido de nuevo')

                redirect(url_for('hello'))

            else:
                flash('Contraseña incorrecta')

        else:
            flash('Usuario no encontrado')

        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('singup', methods=['GET','POST'])
def singup():
    singup_form = LoginForm()
    context = {
        'singup_form': singup_form
    }

    if singup_form.validate_on_submit():
        username = singup_form.username.data
        password = singup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username,password_hash)

            user_put(user_data)

            user = UserModel(user_data)
            login_user(user)

            flash('Ususario registrado con exito')

            return redirect(url_for('hello'))
        else:
            flash('El usuario ya existe')


    return render_template('singup.html', **context)
