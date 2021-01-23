from flask import Flask

# This file is a constructor that pulls all of the parts of the application
# together into a package and then tells Python to treat it as a package.
# Source: https://pythonise.com/series/learning-flask

# Instance of Flask object
app = Flask(__name__)

# Dependencies
from app import database
from app import views
from app import login
from app import profile
from app import tenancy
