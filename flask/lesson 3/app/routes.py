from flask import render_template, request, url_for, redirect, flash
from app import app, db
from app.models import User
from app.forms import RegisterForm, signInForm


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user == True:
            flash("Email or Username already exists", "danger")
            return redirect(url_for("register"))
        
        new_user = User(email = email, username = username, password = password)
        db.session.add(new_user)
        db.session.commit()
        flash("New account created successfuly!", "danger")
        return redirect(url_for("home"))
    
    return render_template("register.html", form = form)