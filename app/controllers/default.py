from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user

from app import app, db
from app.models.forms import LoginForm
from app.models.models import User


@app.route("/home", methods=["GET"])
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = LoginForm(request.form)
        user = User.query.filter_by(username=form.username.data).first()
        if form.validate_on_submit():
            if user is not None and user.password == form.password.data:
                login_user(user)
                return redirect('/home')
            else:
                flash("Invalid username or password.")
                return redirect('/login')
        else:
            return redirect('/login')
    return render_template("login.html", form=LoginForm())


@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect('/login')


@app.route("/create-user", methods=["GET"])
def create_user():
    user = User(fullname="ok", username="ok", email="ok", password="ok")
    db.session.add(user)
    db.session.commit()
    return f"User {user.username} created successfully"


@app.route("/select-and-update-user/<int:id>", methods=["GET"])
def select_user(id: int):
    user = User.query.get(id)
    user.fullname += " - Updated"
    db.session.add(user)
    db.session.commit()
    return f"User {user.fullname} selected and updated successfully"


@app.route("/delete-user/<int:id>", methods=["GET"])
def delete_user(id: int):
    user = User.query.get(id)
    print(user)
    db.session.delete(user)
    db.session.commit()
    return f"User {user.fullname} deleted successfully"
