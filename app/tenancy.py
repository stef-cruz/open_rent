from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
import os
import googlemaps

from app import app
from app.database import DB_TENANCIES

# GOOGLE API KEY
gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))


# ADD TENANCY
@app.route("/add_tenancy", methods=["GET", "POST"])
def add_tenancy():
    """Create tenancy in database and return view tenancy page"""
    if request.method == 'POST':
        if session["user"]:
            # Geocode to get latitude and longitude of address,
            # source https://github.com/googlemaps/google-maps-services-python
            address = request.form.get('address')
            geocode_result = gmaps.geocode(address)
            # Extract lat and long from geocode_result,
            # source https://stackoverflow.com/questions/37311687/extracting-lat-lon-from-geocode-result-list-with-python-google-maps-api
            latitude = geocode_result[0]["geometry"]["location"]["lat"]
            longitude = geocode_result[0]["geometry"]["location"]["lng"]
            tenancy = {
                "address": request.form.get("address"),
                "latitude": latitude,
                "longitude": longitude,
                "accommodation_type": request.form.get("accommodation_type"),
                "start_date": request.form.get("start_date"),
                "end_date": request.form.get("end_date"),
                "price": request.form.get("end_date"),
                "created_by": session["user"]
            }
            DB_TENANCIES.insert_one(tenancy)
            flash("Tenancy Successfully Added")
            return redirect(url_for("view_tenancy"))
        else:
            return redirect(url_for("login"))

    # GET method
    return render_template("add-tenancy.html")


# VIEW TENANCY
@app.route("/view_tenancy")
def view_tenancies():
    tenancies = DB_TENANCIES.find()
    return render_template("view-tenancy.html", tenancies=tenancies)


# EDIT TENANCY


# DELETE TENANCY
