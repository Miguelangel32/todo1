from flask import Flask, render_template, redirect, url_for
from forms import TareaForm

app = Flask(__name__)

app.secret_key = "cualquiercosa"

tareas = ["bar","foo", "baz"]


@app.route("/")
def index():
    return render_template("index.html", tareas=tareas)

@app.route("/agregar/", methods=["GET","POST"])
def agregar():
    form = TareaForm()
    if form.validate_on_submit():
        tarea = form.tarea.data
        tareas.append(tarea)
        return redirect(url_for('index'))
        
    return render_template("agregar.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
