from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from app import app
from app.database import DB_USERS


# PROFILE VIEW
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Fetch username from db and return the user's profile page"""
    username = DB_USERS.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# EDIT PROFILE
@app.route("/edit-profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    return


# UPDATE PROFILE
@app.route("/update-profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    return


# DELETE PROFILE
@app.route("/delete-profile/<username>", methods=["GET", "POST"])
def delete_profile(username):
    return
