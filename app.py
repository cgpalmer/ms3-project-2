# import pymongo
import os
import hashlib
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
comparison_number = None

mongo = PyMongo(app)
# Initial home page
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("home.html", report=mongo.db.report.find().limit(5))

#login page
@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/check_password', methods=['POST'])
def check_password():
    login_email = request.form['login_username']  
    login_password = request.form['login_password']
    print(login_password)
    user = mongo.db.user_credentials.find_one({"user_email": login_email})
    for k,v in user.items():
        if k != "_id":
            if k == 'user_password':
                stored_password = v
                print(stored_password)
            if k == 'salt':
                stored_salt = v
                print("this is the salt")
                print(stored_salt)
  
                hash_login_password = hashlib.pbkdf2_hmac(
                'sha256', # The hash digest algorithm for HMAC
                login_password.encode('utf-8'), # Convert the password to bytes
                stored_salt, # Provide the salt
                100000, # It is recommended to use at least 100,000 iterations of SHA-256 
                dklen=128 # Get a 128 byte key
                )
                print(hash_login_password)
        
                if stored_password == hash_login_password:
                    print("match")
                    return render_template('user_dash.html')
                else:
                    print("no match")
                    return render_template('login.html')

#signup
@app.route('/signup')
def signup():
    return render_template("signup.html")

#signup
@app.route('/creating_user', methods=['POST'])
def creating_user():
    salt = os.urandom(32)
    new_username= request.form['new_username']
    new_password = request.form['new_password']
    list_existing_emails = []
    used_email = mongo.db.user_credentials.find()
    print(used_email)
    for x in used_email:
        print(x["user_email"])
        list_existing_emails.append(x["user_email"])
        print(list_existing_emails)

    
    check_username_availibility = mongo.db.user_credentials.find_one({"user_email": new_username})
    print(check_username_availibility)
    for k,v in check_username_availibility.items():
        if k == "user_email":
            user_email = v
            print(user_email)
    if "user_email" in check_username_availibility:
        return render_template("signup.html")
    else:
        print(new_password)
        hash_new_password = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        new_password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000, # It is recommended to use at least 100,000 iterations of SHA-256 
        dklen=128 # Get a 128 byte key
        )
        mongo.db.user_credentials.insert_one({"user_email": new_username, "user_password": hash_new_password, "salt": salt})
        return render_template("login.html")


# Reading reports

@app.route('/get_report')
def get_report():
    return render_template("report.html", report=mongo.db.report.find())    


# This is the OG screen with one search box as default.
@app.route('/search_report')
def search_report():
    parameter = "Not chosen"
    global comparison_number
    comparison_number = 1
    search_parameter1=mongo.db.search_parameters.find()
    return render_template("searchResults.html", search_parameter1=search_parameter1, parameter=parameter, comparison_number=comparison_number)

# Will search the basic parameters.
@app.route('/search_report_parameter',  methods=["POST"])
def search_report_parameter():
    if request.method == "POST":
     
        parameterChoices=[]
        chosen_parameter_options=[]
        checkedParameters = request.form.getlist("searchParameter")
        print(request.form.getlist("searchParameter"))
        for choice in checkedParameters:
            parameterChoices.append(choice)
            print(parameterChoices)
        for option in parameterChoices:
            options = mongo.db.report.distinct(option)
            print(options)
            chosen_parameter_options.append(options)
            print(chosen_parameter_options)
        number_of_fields = len(chosen_parameter_options)
        return render_template("pickValuesOr.html", number_of_fields=number_of_fields, chosen_parameter_options=chosen_parameter_options, parameterChoices=parameterChoices)

# This submits the final report and returns the reports
@app.route('/retrieving_report', methods=["POST"])
def retrieving_report():
    choices = []
    values = []
    fields = request.form["number_of_fields"]
    number_of_fields = int(fields)
    print(str(number_of_fields))
    for x in range(int(number_of_fields)):
        print(x)
        key = request.form["search_choice{}".format(x)]
        print(key)
        choices.append(key)
        value = request.form["search_value{}".format(x)]
        print(value)
        values.append(value)

        # Return values
    if number_of_fields == 2:
        print("if 2")
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]} ] } )
    elif number_of_fields  == 3:
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]} ] } )
    elif number_of_fields  == 4:
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]} ] } )
    elif number_of_fields  == 5:
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]}, { choices[4] : values[4]} ] } )
    else:
        the_report = mongo.db.report.find( {choices[0]: values[0]})
    return render_template("resultsDisplayBasic.html", report=the_report)


@app.route('/and_filter_parameters',  methods=["POST"])
def and_filter_parameters():
    
    parameterChoices=[]
    chosen_parameter_options=[]
    checkedParameters = request.form.getlist("searchParameter")
    print(request.form.getlist("searchParameter"))
    for choice in checkedParameters:
        parameterChoices.append(choice)
        print(parameterChoices)
    for option in parameterChoices:
        options = mongo.db.report.distinct(option)
        print(options)
        chosen_parameter_options.append(options)
        print(chosen_parameter_options)
    number_of_fields = len(chosen_parameter_options)
    return render_template("pickValuesAnd.html", number_of_fields=number_of_fields, chosen_parameter_options=chosen_parameter_options, parameterChoices=parameterChoices)

@app.route('/retrieving_report_with_filters', methods=["POST"])
def retrieving_report_with_filters():
    choices = []
    values = []
    fields = request.form["number_of_fields"]
    number_of_fields = int(fields)
    print(str(number_of_fields))
    for x in range(int(number_of_fields)):
        print(x)
        key = request.form["search_choice{}".format(x)]
        print(key)
        choices.append(key)
        value = request.form["search_value{}".format(x)]
        print(value)
        values.append(value)

        # Return values
    if number_of_fields == 2:
        print("if 2")
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]} ] } )
    elif number_of_fields  == 3:
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]} ] } )
    elif number_of_fields  == 4:
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]} ] } )
    elif number_of_fields  == 5:
        the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]}, { choices[4] : values[4]} ] } )
    else:
        the_report = mongo.db.report.find( {choices[0]: values[0]})
    return render_template("results_display.html", report=the_report)



@app.route('/compare_by_all',  methods=["POST"])
def compare_by_all():
    parameter = request.form['searchParameter']
    parameter_options = mongo.db.report.distinct(parameter)
    return render_template("pickValuesComparison.html", parameter=parameter, parameter_options=parameter_options)



@app.route('/search_all_by_parameter',  methods=["POST"])
def search_all_by_parameter():
    parameter = request.form['parameter']
    print(parameter)
    parameterValue = request.form['parameterValue']
    print(parameterValue)
    location = request.form['locationValue']
    print(location)
    searches = []
    
    locationValues= mongo.db.report.distinct(location)

    print(locationValues)
  
    for x in range(len(locationValues)):
        the_report = mongo.db.report.find( { "$and": [ {parameter:parameterValue }, {location : locationValues[x]}] } )
        searches.append(the_report)
        print(searches)
    
    amountOfSearches = len(locationValues)

    return render_template("resultsDisplayCompareByAll.html", report=the_report, searches=searches, amountOfSearches=amountOfSearches)
    # return "done"












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





