from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from app.database import MONGO, DB_USERS


# Registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Check if username exists in db
        existing_user = DB_USERS.find_one({
            "username": request.form.get("username").lower()
        })
        # if yes, return user to register function
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # fetch username and password from the form
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        # insert into DB
        DB_USERS.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
    return render_template('register.html')


# Log in
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# Log out