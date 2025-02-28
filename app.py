from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from modelos import Alumno, bd

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == '__main__':
    csrf.init_app(app)
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)