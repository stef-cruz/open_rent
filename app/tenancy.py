from bson.objectid import ObjectId
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
import os
import googlemaps

from app import app
from app.database import DB_TENANCIES, DB_ACCOMMODATION_TYPES, DB_USERS

# GOOGLE API KEY
gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))


# ADD TENANCY
@app.route("/add_tenancy", methods=["GET", "POST"])
def add_tenancy():
    """Create tenancy in database. Checks:
    1- If user is logged in
    2- If address is valid
    3- If address is in Dublin

    :return tenancy added
    """
    if session["user"]:
        if request.method == 'POST':
            # Geocode to get latitude and longitude of address,
            # source https://github.com/googlemaps/google-maps-services-python
            address = request.form.get('address_1')
            geocode_result = gmaps.geocode(address)
            # Extract lat and long from geocode_result,
            # source https://stackoverflow.com/questions/37311687/extracting-lat-lon-from-geocode-result-list-with-python-google-maps-api
            if geocode_result:
                latitude = geocode_result[0]["geometry"]["location"]["lat"]
                longitude = geocode_result[0]["geometry"]["location"]["lng"]
                if 53.25 >= latitude >= 53.35 or -6.36 <= longitude <= -6.26:
                    tenancy = {
                        "address_1": request.form.get("address_1"),
                        "address_2": request.form.get("address_2"),
                        "latitude": latitude,
                        "longitude": longitude,
                        "accommodation_type": request.form.get("accommodation_type"),
                        "start_date": request.form.get("start_date"),
                        "end_date": request.form.get("end_date"),
                        "price": request.form.get("price"),
                        "created_by": session["user"]
                    }
                    DB_TENANCIES.insert_one(tenancy)
                    flash("Tenancy Successfully Added")

                    # get ID from tenancy added
                    tenancy_added = DB_TENANCIES.find_one({'address_1': address})
                    tenancy_id = tenancy_added.get('_id')

                    # display tenancy added
                    return redirect(url_for("view_tenancy", tenancy_id=tenancy_id))

                flash('Please enter an address in Dublin City.')
                return redirect(url_for("add_tenancy"))

            flash('Please enter a valid address.')
            return redirect(url_for("add_tenancy"))

        # Get accommodation type from db
        accommodation_types = DB_ACCOMMODATION_TYPES.find()
        return render_template("add-tenancy.html", accommodation_types=accommodation_types)

    # If user not logged in
    return redirect(url_for("login"))


# VIEW TENANCY
@app.route("/view_tenancy/<tenancy_id>")
def view_tenancy(tenancy_id):
    """Return tenancy added in add_tenancy function"""
    tenancy = DB_TENANCIES.find_one(
        {'_id': ObjectId(tenancy_id)})
    return render_template("view-tenancy.html", tenancy=tenancy)


# EDIT TENANCY
@app.route("/edit_tenancy/<tenancy_id>", methods=["GET", "POST"])
def edit_tenancy(tenancy_id):
    """Edit tenancy in database. Checks:
        1- If user is logged in
        2- If address is valid
        3- If address is in Dublin

        :return edit page
        """

    if session["user"]:
        if request.method == 'POST':
            # Geocode to get latitude and longitude of address,
            # source https://github.com/googlemaps/google-maps-services-python
            address = request.form.get('address_1')
            geocode_result = gmaps.geocode(address)
            # Extract lat and long from geocode_result,
            # source https://stackoverflow.com/questions/37311687/extracting-lat-lon-from-geocode-result-list-with-python-google-maps-api
            if geocode_result:
                latitude = geocode_result[0]["geometry"]["location"]["lat"]
                longitude = geocode_result[0]["geometry"]["location"]["lng"]
                if 53.25 >= latitude >= 53.35 or -6.36 <= longitude <= -6.26:
                    edited_tenancy = {
                        "address_1": request.form.get("address_1"),
                        "address_2": request.form.get("address_2"),
                        "latitude": latitude,
                        "longitude": longitude,
                        "accommodation_type": request.form.get("accommodation_type"),
                        "start_date": request.form.get("start_date"),
                        "end_date": request.form.get("end_date"),
                        "price": request.form.get("price"),
                        "created_by": session["user"]
                    }
                    DB_TENANCIES.update({"_id": ObjectId(tenancy_id)}, edited_tenancy)
                    flash("Tenancy Successfully Updated")

                flash('Please enter an address in Dublin City.')
                return redirect(url_for("edit_tenancy", tenancy_id=tenancy_id))

            flash('Please enter a valid address.')
            return redirect(url_for("edit_tenancy", tenancy_id=tenancy_id))

        # Search for tenancy in DB
        tenancy = DB_TENANCIES.find_one(
            {'_id': ObjectId(tenancy_id)})
        accommodation_types = DB_ACCOMMODATION_TYPES.find()
        return render_template("edit-tenancy.html", tenancy=tenancy, accommodation_types=accommodation_types)

    # If user not logged in
    return redirect(url_for("login"))


# DELETE TENANCY
@app.route("/delete_tenancy/<tenancy_id>")
def delete_tenancy(tenancy_id):
    """Delete tenancy from the database. Check if user is logged in.

        :return user's profile page
        """
    if session["user"]:
        username = DB_USERS.find_one(
            {"username": session["user"]})["username"]
        current_tenancy = DB_TENANCIES.find_one({'_id': ObjectId(tenancy_id)})
        if username == current_tenancy['created_by']:
            DB_TENANCIES.remove({'_id': ObjectId(tenancy_id)})
        flash("Tenancy successfully deleted")
        return redirect(url_for('profile', username=username))
    return redirect(url_for('login_page'))