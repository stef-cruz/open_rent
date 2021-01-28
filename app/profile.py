from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from app import app
from app.database import DB_USERS, DB_TENANCIES


# PROFILE VIEW
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Fetch username from db and return the user's profile page"""
    if session["user"]:
        username = DB_USERS.find_one(
            {"username": session["user"]})["username"]
        user_tenancies = DB_TENANCIES.find({'created_by': username})
        return render_template("profile.html", username=username, user_tenancies=user_tenancies)

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
