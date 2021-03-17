from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__) #Se instancia la aplicación
bootstrap = Bootstrap(app)# se instancia bootstrap

app.config['SECRET_KEY'] = 'SUPER SECRETO' #Se configura una llave secreta



to_dos = ['Comprar pan','Pagar la luz','Dormir']

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


@app.route('/hello') #Ruta en la que se correra la funcion
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'to_dos': to_dos
    } #diccionario con los valores a pasar al template

    return render_template('hello.html', **context) # ** expande el diccionario