from flask import request, make_response, redirect, render_template, session, flash, url_for
from app import create_app
from app.firestore_service import get_users, get_todos, put_todo, delete_todo, update_todo
from flask_login import login_required, current_user
from app.forms import ToDoForm, DeleteToDoForm, UpdateToDoForm
import unittest


app = create_app()


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


@app.route('/hello', methods=['GET','POST']) #Ruta en la que se correra la funcion
@login_required #verifica la presencia del login
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id  #Trae el usuario listo en el login de flask
    todo_form = ToDoForm()
    delete_todo = DeleteToDoForm()
    update_form = UpdateToDoForm()

    context = {
        'user_ip': user_ip,
        'to_dos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_todo': delete_todo,
        'update_todo': update_form
    } #diccionario con los valores a pasar al template

    if todo_form.validate_on_submit():
        put_todo(username, todo_form.descriptrion.data)

        flash('Tu tarea se creó con exito')

        return redirect(url_for('hello'))


    return render_template('hello.html', **context) # ** expande el diccionario

@app.route('/todos/delete/<todo_id>', methods=['POST']) #Las rutas dinamicas pasan parametro y se declaran con <>
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)

    return redirect(url_for('hello'))


@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id

    update_todo(user_id, todo_id, done)

    return redirect(url_for('hello'))

