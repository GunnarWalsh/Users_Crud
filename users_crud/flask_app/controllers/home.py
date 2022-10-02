from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import city

@app.route("/users/new")
def home():
    return render_template("home.html")

@app.route("/users/show")
def show():
    return render_template("show.html" , all_users = city.User.return_users())


@app.route("/users/add_to_db", methods=["POST"])
def add_user_to_db():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    city.User.create_user(data)
    return redirect("/users/show")

@app.route("/user/<int:id>/show")
def show_user(id):
    data = {
        "id" : id
    }
    return render_template("user.html" , return_user = city.User.get_one_user(data))

@app.route("/user/<int:id>/edit")
def edit_user(id):
    data = {
        "id" : id
    }
    return render_template("edit_user.html" , return_user = city.User.get_one_user(data))

@app.route("/user/<int:id>/edit_in_db", methods=["POST"])
def edit_user_in_db(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id,
    }
    city.User.edit_user(data)
    return redirect(f"/user/{id}/show")

@app.route("/user/<int:id>/del_from_db")
def delete_user(id):
    data = {
        "id":id,
    }
    city.User.delete_user(data)
    return redirect("/users/show")