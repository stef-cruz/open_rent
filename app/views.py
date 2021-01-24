from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from app import app


# Index view
@app.route("/")
def index():
    return render_template("index.html")