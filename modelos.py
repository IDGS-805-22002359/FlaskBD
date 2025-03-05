# filepath: /Users/alejandro/Developer/utl/desarrollo web profesional/FlaskBD/modelos.py
from flask_sqlalchemy import SQLAlchemy
import datetime

bd = SQLAlchemy()

class Alumno(bd.Model):
    __tablename__ = 'alumnos'
    
    id = bd.Column(bd.Integer, primary_key=True)
    foto = bd.Column(bd.String(255), nullable=True)
    matricula = bd.Column(bd.String(8), unique=True, nullable=False)
    nombre = bd.Column(bd.String(50), nullable=False)
    apellidos = bd.Column(bd.String(50), nullable=False)
    email = bd.Column(bd.String(50), unique=True, nullable=False)
    password = bd.Column(bd.String(50), nullable=False)
    created_at = bd.Column(bd.DateTime, default=datetime.datetime.now)