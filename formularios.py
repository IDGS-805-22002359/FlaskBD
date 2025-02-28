from wtforms import Form, StringField, SubmitField, FieldList, RadioField, SelectField, IntegerField, PasswordField, EmailField, DateField
from wtforms import validators
from datetime import datetime

class Alumno(Form):
    
    matricula = StringField('Matrícula', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=8, max=8, message='La matrícula debe tener 8 caracter.es')
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
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=8, max=50, message='La contraseña debe tener entre 8 y 50 caracteres.')
    ])
    
def validar_anio(form, field):
    hoy = datetime.today()
    fecha = field.data
    if(fecha.year < 1936):
        raise validators.ValidationError('El año de nacimiento debe ser mayor a 1936.')
    if(hoy.year - fecha.year - ((hoy.month, hoy.day) < (fecha.month, fecha.day)) < 0):
        raise validators.ValidationError('La fecha de nacimiento no puede ser mayor a la fecha actual.')
    
class Zodiaco(Form):
    
    nombre = StringField('Nombre', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=3, max=50, message='El nombre debe tener entre 3 y 50 caracteres.')
    ])
    apellido_paterno = StringField('Apellido Paterno', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=3, max=50, message='El apellido paterno debe tener entre 3 y 50 caracteres.')
    ])
    apellido_materno = StringField('Apellido Materno', [
        validators.DataRequired('Este campo es requerido.'),
        validators.Length(min=3, max=50, message='El apellido materno debe tener entre 3 y 50 caracteres.')
    ])
    fecha_nacimiento = DateField('Fecha de Nacimiento', [
        validators.DataRequired('Este campo es requerido.'),
        validar_anio
    ])
    sexo = RadioField('Sexo', choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ], validators=[
        validators.DataRequired('Este campo es requerido.')
    ])
    
    
    