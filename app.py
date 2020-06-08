# import pymongo
import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

from os import path
if path.exists("env.py"):
    import env

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = "projectDB"
COLLECTION_NAME = "report"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_report')
def get_report():
    return render_template("report.html", report=mongo.db.report.find())
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

