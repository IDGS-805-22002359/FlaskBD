from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from modelos import Alumno, bd
import formularios

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def listar_alumnos():
    id = request.args.get('id')
    if id:
        alumno = Alumno.query.get_or_404(id)
        return render_template("alumno_tarjeta.html", alumno=alumno)
    formulario = formularios.Alumno(request.form)
    alumnos = Alumno.query.all()
    return render_template("alumnos.html", formulario=formulario, alumnos=alumnos, id=id)


@app.route("/alumno", methods=["GET", "POST"])
def crear_alumno(id):
    formulario = formularios.Alumno(request.form)

    if request.method == "POST":
        if formulario.validate():
            alumno = Alumno()
            formulario.populate_obj(alumno)
            bd.session.add(alumno)
            bd.session.commit()
            flash("Alumno creado exitosamente.", "success")
            return redirect(url_for("index"))
        else:
            flash("Error al crear el alumno. Verifique los datos.", "danger")

    return render_template("alumno.html", formulario=formulario)

@app.route("/alumno/<int:id>", methods=["GET", "POST"])
def editar_alumno(id):
    alumno = Alumno.query.get_or_404(id)
    formulario = formularios.Alumno(request.form, obj=alumno)

    if request.method == "POST":
        if formulario.validate():
            formulario.populate_obj(alumno)
            if not formulario.password.data:
                del formulario.password
            bd.session.commit()
            flash("Alumno actualizado exitosamente.", "success")
            return redirect(url_for("index"))
        else:
            flash("Error al actualizar el alumno. Verifique los datos.", "danger")

    return render_template("alumno.html", formulario=formulario, alumno=alumno)

@app.route("/alumno/eliminar/<int:id>", methods=["POST"])
def eliminar_alumno(id):
    alumno = Alumno.query.get_or_404(id)
    bd.session.delete(alumno)
    bd.session.commit()
    flash("Alumno eliminado exitosamente.", "success")
    return redirect(url_for("index"))

if __name__ == '__main__':
    csrf.init_app(app)
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)