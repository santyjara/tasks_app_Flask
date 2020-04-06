from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Formulario de entrada


class loginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class todoForm(FlaskForm):
    description = StringField('Ingrese la descripcion de la tarea',validators=[DataRequired()])
    submit = SubmitField('Registrar tarea')


class DeleteForm(FlaskForm):
    submit = SubmitField('Borrar tarea')


class UpdateForm(FlaskForm):
    submit = SubmitField('Actualizar')


