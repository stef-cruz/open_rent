from flask import Flask

# This file is a constructor that pulls
# all of the parts of our application
# together into a package and then tells
# Python to treat it as a package!

# Instance of Flask object
app = Flask(__name__)

# Dependencies
from app import database
from app import views
