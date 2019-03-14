

import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#Set up

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect the database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


Base.classes.keys()



# Save reference to the table
Station = Base.classes.station
Measurements = Base.classes.measurement



# Create our session (link) from Python to the DB
session = Session(engine)



# Flask Routes
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return ( 'hi')

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculated the date 1 year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Date 12 months ago
    p_results = session.query(Measurements.date, func.avg(Measurements.prcp)).filter(Measurements.date >= one_year_ago).group_by(Measurements.date).all()
    #print(p_results)
    return jsonify(p_results)

@app.route("/api/v1.0/stations")
def stations():
    s_results = session.query(Station.station, Station.name).all()
    return jsonify(s_results)

@app.route("/api/v1.0/tobs")
def tobs():
    # Calculated the date 1 year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    t_results = session.query(Measurements.date, Measurements.station, Measurements.tobs).filter(Measurements.date >= one_year_ago).all()
    return jsonify(t_results)

@app.route("/api/v1.0/2016-08-23")
def startDateOnly():
    day_temp_results = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).filter(Measurements.date >= '2016-08-23').all()
    return jsonify(day_temp_results)
    # return date

@app.route("/api/v1.0/2016-02-15/2016-02-28")
def startDateEndDate():
    multi_day_temp_results = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).filter(Measurements.date >= '2016-02-15').filter(Measurements.date <= '2016-02-28').all()
    return jsonify(multi_day_temp_results)

if __name__ == "__main__":
    app.run(debug=True)



