from flask import (render_template,session)

from app import app
from app.database import DB_USERS


# Index view
@app.route("/contact")
def contact():
    if session:
        username = DB_USERS.find_one(
            {"username": session["user"]})["username"]
        return render_template("contact.html", username=username)
    return render_template("contact.html")