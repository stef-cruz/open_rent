from flask import (render_template, session, redirect, url_for)

from app import app
from app.database import DB_USERS


# Index view
@app.route("/")
def index():
    if session:
        username = DB_USERS.find_one(
            {"username": session["user"]})["username"]
        return render_template("index.html", username=username)
    return render_template("index.html")