# import pymongo
import os
from flask import Flask, render_template, url_for, request, redirect, session
from os import path
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'thefluffiestofdogs'

if path.exists("env.py"):
    import env

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = "projectDB"


mongo = PyMongo(app)
# Initial home page
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("home.html", report=mongo.db.report.find().limit(5))

# Reading reports

@app.route('/get_report')
def get_report():
    return render_template("report.html", report=mongo.db.report.find())

@app.route('/search_report')
def search_report():
    search_parameters_email = mongo.db.report.find()
    search_parameters_username = mongo.db.report.find()
    search_parameters_category_name = mongo.db.report.find()
    search_parameters_city = mongo.db.report.find()
    search_parameters_sub_category = mongo.db.report.find()
    search_parameters_street = mongo.db.report.find()
    search_parameters_types = mongo.db.search_parameters.find()
    categories = mongo.db.categories.find()
    sub_category = mongo.db.sub_category.find()
    return render_template("searchResults.html", sp_types=search_parameters_types, sub_category=sub_category, categories=categories, sp_street=search_parameters_street, sp_sub_category=search_parameters_sub_category, sp_city=search_parameters_city, sp_category=search_parameters_category_name, sp_email=search_parameters_email, sp_username=search_parameters_username)

# @app.route('/results_display', methods=["POST"])
# def results_display():
#     identifier = request.form["search_identifier"]
#     # email = request.form["search_email"]
#     # username = request.form["search_username"]
  
#     # if  == "":
#     #     the_report = mongo.db.report.find({"username": username})
#     # else:
#     #     the_report = mongo.db.report.find({"$or": [{"email": email}, {"username": username}]})
#     return render_template("results_display.html", report=the_report, email=email, username=username)


@app.route('/results_display', methods=["POST"])
def results_display():
    # find the value of the field "search_identifier"
    # they key must equal the name of the field it will search in
    key = request.form["search_parameter"]
    # value must be the value posted from the input
    value = request.form["search_value"]
    the_report = mongo.db.report.find({key: value})
    return render_template("results_display.html", report=the_report, key=key, value=value)

# Adding reports

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



# Updating reports
@app.route('/user_modify/<report_id>')
def user_modify(report_id):
    the_report = mongo.db.report.find_one({"_id": ObjectId(report_id)})
    available_categories = mongo.db.categories.find()
    available_sub_categories = mongo.db.sub_category.find()
    return render_template('user_modify.html', report=the_report, categories=available_categories, sub_category=available_sub_categories)

@app.route('/edit_report/<report_id>', methods=["POST"])
def edit_report(report_id):
    report = mongo.db.report
    report.update({'_id': ObjectId(report_id)},
                  {
                  'email': request.form.get('email'),
                  'username': request.form.get('username'),
                  'category_name': request.form.get('category_name'),
                  'new_category_name': request.form.get('new_category_name'),
                  'sub_category': request.form.get('sub_category'),
                  'new_sub_category': request.form.get('new_sub_category'),
                  'incident_description': request.form.get('incident_description'),
                  'building': request.form.get('building'),
                  'street': request.form.get('street'),
                  'city': request.form.get('city'),
                  'county': request.form.get('county'),
                  'postcode': request.form.get('postcode'),
                  'report_to_authorities': request.form.get('report_to_authorities')
                  })
    return redirect(url_for('get_report'))


# Deleting reports

@app.route('/confirm_delete_report/<report_id>')
def confirm_delete_report(report_id):
    the_report = mongo.db.report.find_one({"_id": ObjectId(report_id)})
    available_categories = mongo.db.categories.find()
    available_sub_categories = mongo.db.sub_category.find()

    return render_template('confirm_delete.html', report=the_report, categories=available_categories, sub_category=available_sub_categories)


@app.route('/delete_report/<report_id>', methods=["POST"])
def delete_report(report_id):
    # Trigger a modal of some kind where the user has to input the correct email.
    report = mongo.db.report
    report.update({'_id': ObjectId(report_id)}, {"$set": {"archive_report": request.form.get('archive')}})
    return redirect(url_for('get_report'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

