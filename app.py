# from flask import Flask

# app = Flask(__name__)
# You probably noticed the __name__ variable inside of the Flask() function. 
# Let's pause for a second and identify what's going on here.
# 
# This __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine if your code is being run 
# from the command line or if it has been imported into another piece of code. 
# Variables with underscores before and after them are called magic methods in Python.

# @app.route('/')
# def hello_world():
#     return 'Hello world'

# CMD: export FLASK_APP=app.py
# This command sets the FLASK_APP environment variable to the name of our Flask file, app.py.


import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# When creating routes, we follow the naming convention /api/v1.0/ 
# followed by the name of the route. This convention signifies that 
# this is version 1 of our application. This line can be updated to 
# support future versions of the app as well.

@app.route("/api/v1.0/precipitation")
