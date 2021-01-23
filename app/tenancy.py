from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from app import app
from app.database import DB_TENANCIES


@app.route("/add_tenancy")
def add_tenancy():
    return render_template("add-tenancy.html")


@app.route("/view_tenancy")
def view_tenancies():
    tenancies = DB_TENANCIES.find()
    return render_template("view-tenancy.html", tenancies=tenancies)