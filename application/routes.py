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
# from config import dbusername, dbpassword


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

# @app.route("/projectone") #need this to be a page in itself#
# def projectone():
#     return render_template("projectone.html")

# @app.route("/projecttwo")
# def projecttwo():
#     return render_template("projecttwo.html")

@app.route("/projectetl")
def projectetl():
    return render_template("projectetl.html")

@app.route("/projectsql")
def projectsql():
    return render_template("projectsql.html")

@app.route("/capstone")
def capstone():
    return render_template("capstone.html")

# @app.route("/finalproject")
# def finalproject():
#     return render_template("finalproject.html")

@app.route("/blog")
def blog():
    coursestaken = [{"Title ":{"0":"Applied Data Science Capstone","1":"Databases and SQL for Data Science","2":"Data Science Methodology","3":"Data Visualization with Python","4":"Machine Learning with Python","5":"What is Data Science?","6":"Python for Data Science and AI","7":"Tools for Data Science","8":"Data Analysis with Python","9":"Front-End Web UI Frameworks and Tools: Bootstrap 4"},"Decription":{"0":"In this course, we will meet some data science practitioners and we will get an overview of what data science is today.","1":"In this course will create a final project with a Jupyter Notebook on IBM Data Science Experience and demonstrate your proficiency preparing a notebook, writing Markdown, and sharing your work with your peers.","2":"\u00a0In this course, you will learn: - The major steps involved in tackling a data science problem. - The major steps involved in practicing data science, from forming a concrete business or research problem, to collecting and analyzing data, to building a model, and understanding the feedback after model deployment.","3":"This course will take you from zero to programming in Python in a matter of hours\u2014no prior programming experience necessary! You will learn Python fundamentals, including data structures and data analysis, complete hands-on exercises throughout the course modules, and create a final project to demonstrate your new skills. By the end of this course, you\u2019ll feel comfortable creating basic programs, working with data, and solving real-world problems in Python","4":"The purpose of this course is to introduce relational database concepts and help you learn and apply foundational knowledge of the SQL language. It is also intended to get you started with performing SQL access in a data science environment.","5":"Topics covered: 1) Importing Datasets 2) Cleaning the Data 3) Data frame manipulation 4) Summarizing the Data 5) Building machine learning Regression models 6) Building data pipelines Data Analysis with Python will be delivered through lecture, lab, and assignments.","6":"\u00a0Learning how to leverage a software tool to visualize data will also enable you to extract information, better understand the data, and make more effective decisions. The main goal of this Data Visualization with Python course is to teach you how to take data that at first glance has little meaning and present that data in a form that makes sense to people.","7":"What you\u2019ll get. 1) New skills to add to your resume, such as regression, classification, clustering, sci-kit learn and SciPy 2) New projects that you can add to your portfolio, including cancer detection, predicting economic trends, predicting customer churn, recommendation engines, and many more. 3) And a certificate in machine learning to prove your competency, and share it anywhere you like online or offline, such as LinkedIn profiles and social media.","8":"You will learn how to make RESTful API calls to the Foursquare API to retrieve data about venues in different neighborhoods around the world. You will also learn how to be creative in situations where data are not readily available by scraping web data and parsing HTML code. You will utilize Python and its pandas library to manipulate data, which will help you refine your skills for exploring and analyzing data","9":"client-side web UI frameworks, in particular Bootstrap 4"},"Location":{"0":"coursera","1":"coursera","2":"coursera","3":"coursera","4":"coursera","5":"coursera","6":"coursera","7":"coursera","8":"coursera","9":"coursera"}}]
    return render_template("blog.html", coursestaken=coursestaken)

@app.route("/contact")
def contact():
    return render_template("contact.html")

