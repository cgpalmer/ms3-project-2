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

# Look into why test can't be 0? 
extra_parameters = None

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


# This is the OG screen with one search box as default.
@app.route('/search_report')
def search_report():
    parameter = "Not chosen"
    global extra_parameters
    extra_parameters = 0
    search_parameter1=mongo.db.search_parameters.find()
    return render_template("searchResults.html", search_parameter1=search_parameter1, parameter=parameter, extra_parameters=extra_parameters)


# Tells the computer how many extra boxes we need.
@app.route('/adding_search_parameter')
def adding_search_parameter():
    global extra_parameters
    # turn test to number first.
    extra_parameters = extra_parameters + 1
    return redirect(url_for('search_report_2'))

# You need to make a 'remove parameter'

# Will add in extra parameter boxes. This is neccessary as the og search_report needs to reset the test value.
@app.route('/search_report_2')
def search_report_2():
    global extra_parameters
    parameter = "Not chosen"
    search_parameter1=mongo.db.search_parameters.find()
    return render_template("searchResults.html", search_parameter1=search_parameter1, parameter=parameter, extra_parameters=extra_parameters)

# Will search two parameters.
@app.route('/search_report_parameter',  methods=["POST"])
def search_report_parameter():
    global extra_parameters
    number_of_parameter_fields = int(extra_parameters) + 1
    chosen_parameter_options = []
    chosen_parameters = []
    for x in range(number_of_parameter_fields):
        parameter = request.form["search_parameter{}".format(x)]
        pushParameter = str(parameter)
        chosen_parameters.append(pushParameter)
        parameterChoice = mongo.db.report.distinct(parameter)
        pushParameterChoice = parameterChoice
        chosen_parameter_options.append(pushParameterChoice)
        
    return render_template("searchResults.html", extra_parameters=extra_parameters, chosen_parameter_options=chosen_parameter_options, chosen_parameters=chosen_parameters)

# This submits the final report and returns the reports
@app.route('/retrieving_report', methods=["POST"])
def retrieving_report():
    global extra_parameters
    choices = []
    values = []

    for x in range(-1, extra_parameters):
        key = request.form["search_choice{}".format(x+1)]
        choices.append(key)
        value = request.form["search_value{}".format(x+1)]
        values.append(value)

    # Return values
    if extra_parameters == 1:
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]} ] } )
    elif extra_parameters == 2:
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]} ] } )
    elif extra_parameters == 3:
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]} ] } )
    elif extra_parameters == 4:
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]}, { choices[4] : values[4]} ] } )
    else:
        the_report = mongo.db.report.find( {choices[0]: values[0]})
    return render_template("results_display.html", report=the_report)



@app.route('/checkbox', methods=["GET","POST"])
def checkbox():
    if request.method == "POST":
        z=[]
        w=[]
        selected_users = request.form.getlist("searchParameter")
        print(request.form.getlist("searchParameter"))
        for i in selected_users:
            z.append(i)
            print(z)
        for j in z:
            values = mongo.db.report.distinct(j)
            w.append(values)
            print(w)
        return "done"





















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





