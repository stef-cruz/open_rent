import os
from datetime import date

from app import app
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

# MongoDB credentials
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

MONGO = PyMongo(app)

# Set database collections as constants
DB_USERS = MONGO.db.users
DB_TENANCIES = MONGO.db.tenancies
DB_ACCOMMODATION_TYPES = MONGO.db.accommodation_types

# Today's date
TODAY_DATE = date.today().strftime("%d/%b/%Y")
