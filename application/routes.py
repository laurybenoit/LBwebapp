from application import app
from flask import render_template
from flask import url_for
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import json
import csv
import psycopg2
from sqlalchemy import create_engine
from config import dbusername, dbpassword


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/projectone") #need this to be a page in itself#
def projectone():
    return render_template("projectone.html")

@app.route("/projecttwo")
def projecttwo():
    return render_template("projecttwo.html")

@app.route("/projectetl")
def projectetl():
    return render_template("projectetl.html")

@app.route("/projectsql")
def projectsql():
    return render_template("projectsql.html")

@app.route("/finalproject")
def finalproject():
    return render_template("finalproject.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

