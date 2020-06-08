import pymongo
import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

from os import path
if path.exists("env.py"):
    import env

app.config["MONGODB_URI"] = os.environ.get('MONGO_URI')
app.config["DBS_NAME"] = "projectDB"
# COLLECTION_NAME = "report"

mongo = PyMongo(app)

@app.route('/')
def hello():
    return "Hello world"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)





