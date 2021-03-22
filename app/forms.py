from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nombre de ususario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class ToDoForm(FlaskForm):
    descriptrion = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')

class DeleteToDoForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateToDoForm(FlaskForm):
    submit = SubmitField('Actualizar')