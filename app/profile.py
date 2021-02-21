from bson.objectid import ObjectId
from flask import (
    flash, render_template,
    redirect, session, url_for, request)

from app import app
from app.database import DB_USERS, DB_TENANCIES


# PROFILE VIEW
@app.route("/profile")
def profile():
    """Fetch username from db and return the user's profile page
    source: https://pythonise.com/series/learning-flask/flask-session-object"""

    # User exists in DB
    if not session.get("user") is None:
        username = session["user"]

        # Fetch user, user tenancies and details
        current_user = DB_USERS.find_one({'username': username})
        user_id = current_user.get('_id')
        user_tenancies = DB_TENANCIES.find({'created_by': username})
        user_details = DB_USERS.find_one({'_id': ObjectId(user_id)})

        return render_template("profile.html", current_user=current_user, user_tenancies=user_tenancies,
                               user_details=user_details)

    else:
        return redirect(url_for("login"))


# EDIT PROFILE
@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    """Edit profile in database. Checks:
        1- If user is logged in

        :return edit page
        """
    if not session.get("user") is None:
        username = session["user"]

        if request.method == 'POST':
            DB_USERS.update_one(
                {'_id': ObjectId(user_id)},
                {"$set": {"first_name": request.form.get("first_name"),
                          "last_name": request.form.get("last_name"),
                          "email_address": request.form.get("email_address")}
                 })
            flash("Profile Successfully Updated")

        # Search for user id in DB
        user_details = DB_USERS.find_one({'_id': ObjectId(user_id)})
        return render_template("edit-profile.html", user_details=user_details, username=username)

    else:
        return redirect(url_for("login"))


# DELETE PROFILE
@app.route("/delete_profile/<user_id>", methods=["GET", "POST"])
def delete_profile(user_id):
    """Delete profile from the database. Checks:
    1- If user logged in
    2- If session username is who is logged in

        :return login page
        """
    if not session.get("user") is None:
        username = session["user"]

        current_user = DB_USERS.find_one({'_id': ObjectId(user_id)})
        if username == current_user['username']:
            DB_USERS.remove({'_id': ObjectId(user_id)})
            session.pop("user")
        return redirect(url_for('index'))

    else:
        return redirect(url_for('login'))
