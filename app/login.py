from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from app.database import MONGO, DB_USERS


# REGISTER FUNCTION
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        if request.form.get('confirm-password') != request.form.get('password'):
            flash("Password does not match, try again.")
            return redirect(url_for("register"))

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
        return redirect(url_for("profile", username=session["user"]))

    # GET method, if user is already registered
    return render_template('register.html')


# LOG IN FUNCTION
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # check if username exists in db
        existing_user = DB_USERS.find_one(
            {"username": request.form.get("username").lower()})
        # if user in DB
        if existing_user:
            # check if password supplied matches db
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                # if matches, log in
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))
    # GET method
    return render_template('login.html')


# LOG OUT FUNCTION
@app.route("/logout")
def logout():
    # remove user session from cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))