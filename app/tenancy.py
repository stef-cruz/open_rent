from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
import os

from app import app
from app.database import DB_TENANCIES


# GOOGLE API KEY
app.config["GOOGLE_API"] = os.environ.get('GOOGLE_API')


# ADD TENANCY
@app.route("/add_tenancy")
def add_tenancy():
    if session["user"]:
        return render_template("add-tenancy.html")
    else:
        return redirect(url_for("login"))


# VIEW TENANCY
@app.route("/view_tenancy")
def view_tenancies():
    tenancies = DB_TENANCIES.find()
    return render_template("view-tenancy.html", tenancies=tenancies)


# EDIT TENANCY


# DELETE TENANCY
