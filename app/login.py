from flask import render_template, session, request, redirect, url_for

from app import app
from app.database import MONGO, DB_USERS


# Registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')


# Log in

# Log out