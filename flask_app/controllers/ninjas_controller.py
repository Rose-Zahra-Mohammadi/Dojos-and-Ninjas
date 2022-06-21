from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo
# @app.route("/")
# def index():
#     return redirect("/ninjas")
@app.route("/ninjas")
def ninjas():
    dojo_list = Dojo.read_all()
    return render_template("new_ninja.html", dojo_list = dojo_list)

@app.route("/dojos/new_ninja", methods = ["POST"])
def new_ninja():
    Ninja.create_ninja(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')
