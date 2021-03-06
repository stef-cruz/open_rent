from flask import render_template, session

from app import app
from app.database import DB_USERS


# 404 Not found
@app.errorhandler(404)
def page_not_found(e):
    """ Returns 404 not found template"""
    if not session.get("user") is None:
        username = session["user"]
        current_user = DB_USERS.find_one({'username': username})
        return render_template('404.html', current_user=current_user), 404
    else:
        return render_template('404.html'), 404


# 500 internal server error
@app.errorhandler(500)
def page_not_found(e):
    """ Returns 500 internal server error template"""
    if not session.get("user") is None:
        username = session["user"]
        current_user = DB_USERS.find_one({'username': username})
        return render_template('500.html', current_user=current_user), 500
    else:
        return render_template('500.html'), 500
