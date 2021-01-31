from bson.objectid import ObjectId
from flask import (
    flash, render_template,
    redirect, session, url_for, request)

from app import app
from app.database import DB_USERS, DB_TENANCIES


# PROFILE VIEW
@app.route("/profile")
def profile():
    """Fetch username from db and return the user's profile page"""
    if session["user"]:
        username = DB_USERS.find_one(
            {"username": session["user"]})["username"]
        current_user = DB_USERS.find_one({'username': username})
        user_id = current_user.get('_id')
        user_tenancies = DB_TENANCIES.find({'created_by': username})
        user_details = DB_USERS.find_one({'_id': ObjectId(user_id)})

        return render_template("profile.html", username=username, user_tenancies=user_tenancies,
                               user_details=user_details)

    return redirect(url_for("login"))


# EDIT PROFILE
@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    """Edit profile in database. Checks:
        1- If user is logged in

        :return edit page
        """
    if session["user"]:
        if request.method == 'POST':
            DB_USERS.update_one({'_id': ObjectId(user_id)},
                                {"$set": {"first_name": request.form.get("first_name"),
                                          "last_name": request.form.get("last_name"),
                                          "email_address": request.form.get("email_address")}}
                                )
            # edited_profile = {
            #     "username": request.form.get("username"),
            #     "first_name": request.form.get("first_name"),
            #     "last_name": request.form.get("last_name"),
            #     "email_address": request.form.get("email_address")}
            # DB_USERS.update({"_id": ObjectId(user_id)}, edited_profile)
            flash("Profile Successfully Updated")

        # Search for user id in DB
        user_details = DB_USERS.find_one({'_id': ObjectId(user_id)})
        return render_template("edit-profile.html", user_details=user_details)

    return redirect(url_for("login"))



# DELETE PROFILE
@app.route("/delete_profile/<username>", methods=["GET", "POST"])
def delete_profile(username):
    return
