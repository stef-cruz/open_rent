from flask import render_template

from app import app


# 404 Not found
@app.errorhandler(404)
def page_not_found(e):
    """ Returns 404 not found template"""
    return render_template('404.html'), 404


# 500 internal server error
@app.errorhandler(500)
def page_not_found(e):
    """ Returns 505 internal server error template"""
    return render_template('500.html'), 500