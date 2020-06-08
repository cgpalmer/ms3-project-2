import pymongo
import os

from flask import Flask
app = Flask(__name__)

from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.environ.get('MONGO_URI')
DBS_NAME = "projectDB"
COLLECTION_NAME = "report"

@app.route('/')
def hello():
    return "Hello world"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)



def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

