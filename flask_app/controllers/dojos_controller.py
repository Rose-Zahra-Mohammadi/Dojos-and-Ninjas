# from crypt import methods
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojos_model import Dojo
@app.route("/")
@app.route("/dojos")
def display_dojos():
    dojo_list = Dojo.read_all()
    return render_template("dojos.html", dojo_list = dojo_list)
@app.route("/dojos/dojo_show")
def display_create_dojo():
    return render_template("dojo_show.html")

@app.route("/dojos/new_dojo", methods =['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route("/dojos/<int:id>")
def get_dojo_by_id(id):
    data = {
        "id" : id
    }
    one_dojo =Dojo.get_list(data)
    return render_template("dojo_show.html", one_dojo = one_dojo)

