from wtforms import Form, StringField, SubmitField, PasswordField, EmailField
from wtforms import validators

class Alumno(Form):
    matricula = StringField('Matrícula', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=8, max=8, message='La matrícula debe tener 8 caracteres.')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=3, max=50, message='El nombre debe tener entre 3 y 50 caracteres.')
    ])
    apellidos = StringField('Apellidos', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=3, max=50, message='Los apellidos deben tener entre 3 y 50 caracteres.')
    ])
    email = EmailField('Email', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Email('Email inválido.'),
        validators.Length(min=3, max=50, message='El email debe tener entre 3 y 50 caracteres.')
    ])
    password = PasswordField('Contraseña', [
        validators.Optional(),
        validators.Length(min=8, max=50, message='La contraseña debe tener entre 8 y 50 caracteres.')
    ])
    submit = SubmitField('Guardar')
    delete = SubmitField('Eliminar')