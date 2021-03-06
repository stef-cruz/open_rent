from flask import (render_template, session)

from app import app
from app.database import DB_USERS


# Index view
@app.route("/")
def index():
    if not session.get("user") is None:
        username = session["user"]

        current_user = DB_USERS.find_one({'username': username})
        return render_template("index.html", current_user=current_user)

    else:
        return render_template("index.html")
