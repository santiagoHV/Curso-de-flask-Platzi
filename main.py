from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from Login import LoginForm
import unittest

app = Flask(__name__) #Se instancia la aplicación
bootstrap = Bootstrap(app)# se instancia bootstrap

app.config['SECRET_KEY'] = 'SUPER SECRETO' #Se configura una llave secreta



to_dos = ['Comprar pan','Pagar la luz','Dormir']

@app.cli.command() #Hace que el nombre de la funcion sea un comando
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error = error, error_code = 404)

@app.errorhandler(500)
def not_found(error):
    return render_template('error.html', error = error, error_code = 500)


@app.route('/')
def index():
    user_ip = request.remote_addr #Obtiene de request la ip local

    response = make_response(redirect('/hello')) #crea una redireccion usando response a la ruta especificada

    session['user_ip'] = user_ip #Se manda el valor por sesion


    return response


@app.route('/hello', methods=['GET', 'POST']) #Ruta en la que se correra la funcion
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'to_dos': to_dos,
        'login_form': login_form,
        'username': username
    } #diccionario con los valores a pasar al template

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con exito') #Manda un mensaje tipo alert

        return redirect(url_for('index'))

    return render_template('hello.html', **context) # ** expande el diccionario