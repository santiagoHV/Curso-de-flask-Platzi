from flask import Flask, request, make_response, redirect

app = Flask(__name__) #Se instancia la aplicación

@app.route('/')
def index():
    user_ip = request.remote_addr #Obtiene de request la ip local

    response = make_response(redirect('/hello')) #crea una redireccion usando response a la ruta especificada
    response.set_cookie('user_ip', user_ip) #Crea una cookie y manda la ip en string

    return response


@app.route('/hello') #Ruta en la que se correra la funcion
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'Hello flask, tu IP es {user_ip}'