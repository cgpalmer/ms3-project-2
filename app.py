# import pymongo
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

from os import path
if path.exists("env.py"):
    import env

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = "projectDB"
# COLLECTION_NAME = "report"

mongo = PyMongo(app)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("home.html", report=mongo.db.report.find())

@app.route('/get_report')
def get_report():
    return render_template("report.html", report=mongo.db.report.find())

@app.route('/add_report')
def add_report():
    return render_template("add_report.html", categories=mongo.db.categories.find(),
                           sub_category=mongo.db.sub_category.find(),
                           )

@app.route('/insert_report', methods=['POST'])
def insert_report():
    report = mongo.db.report
    report.insert_one(request.form.to_dict())
    return redirect(url_for('homepage'))


@app.route('/insert_user', methods=['POST'])
def insert_user():
    user = mongo.db.user_credentials
    user.insert_one(request.form.to_dict())
    return redirect(url_for('user_dash'))


@app.route('/signup_page')
def signup_page():
    return render_template("signup.html")

@app.route('/login_page')
def login_page():
    return render_template("login.html")


@app.route('/enter_username')
def enter_username():
    try:
        doc = mongo.db.user_credentials.find_one({'username': login_username.lower()})
        return render_template('enter_template.html')
    except:
        print("Error")

    if not doc:
        return render_template('login.html')


@app.route('/enter_password')
def enter_password():
    # Get the username from the login page
    # Check it exists
    # Retrieve the password for that user name
    # Check the input of the password against the password for that username.
    return render_template("enter_password.html")


@app.route('/user_dash')
def user_dash():
    return render_template("user_dash.html", user=mongo.db.user_credentials.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

