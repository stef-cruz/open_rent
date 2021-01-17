from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from app import app
from app.database import DB_USERS


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # fetch username from db
    username = DB_USERS.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))