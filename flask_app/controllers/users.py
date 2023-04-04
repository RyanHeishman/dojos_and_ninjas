from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def get_all():
    users = User.get_all()
    print(users)
    return render_template("readall.html", all_users = users)

@app.route('/users/new')
def new_user():
    return render_template("newuser.html")

@app.route('/users/new', methods=["POST"])
def create_new_user():
    User.save(request.form)
    return redirect("/users")

@app.route('/users/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show.html" ,user = User.get_one(data))

@app.route('/users/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit.html", user = User.get_one(data))

@app.route('/users/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')
