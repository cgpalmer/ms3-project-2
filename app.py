# import pymongo
import os, math
import hashlib
from flask import Flask, render_template, url_for, request, redirect, session, flash, jsonify
from os import path
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import re
from validate_email import validate_email

app = Flask(__name__)
app.secret_key = 'thefluffiestofwoofers'

if path.exists("env.py"):
    import env

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = "projectDB"




# Look into why test can't be 0? 
comparison_number = None

mongo = PyMongo(app)

def is_new_password_valid(new_password):
    print("function activated")
    while True:   
        if (len(new_password)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", new_password): 
            flag = -1
            break
        elif not re.search("[A-Z]", new_password): 
            flag = -1
            break
        elif not re.search("[0-9]", new_password): 
            flag = -1
            break
        elif re.search("\s", new_password): 
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password") 
            break
    print("flag value in function")
    print(flag)
    return flag

def get_user_password(current_user):
    for k,v in current_user.items():
        if k == 'user_password':
            user_password = v
            print("this has been reach")
            print(user_password)
    return user_password

def get_user_password_salt(current_user):
    for k,v in current_user.items():
        if k == 'salt':
            stored_salt = v
            print("this is the salt")
            print(stored_salt)
    return stored_salt

def get_user_login_name(current_user):
    for k,v in current_user.items():
        login_name = v
    return login_name

def hash_a_password_to_check_it_is_correct(stored_salt, login_password):
    hash_login_password = hashlib.pbkdf2_hmac(
                    'sha256', # The hash digest algorithm for HMAC
                    login_password.encode('utf-8'), # Convert the password to bytes
                    stored_salt, # Provide the salt
                    100000, # It is recommended to use at least 100,000 iterations of SHA-256 
                    dklen=128 # Get a 128 byte key
                )
    return hash_login_password

def hashing_a_new_password(new_password, salt):
    hash_new_password = hashlib.pbkdf2_hmac(
            'sha256', # The hash digest algorithm for HMAC
            new_password.encode('utf-8'), # Convert the password to bytes
            salt, # Provide the salt
            100000, # It is recommended to use at least 100,000 iterations of SHA-256 
            dklen=128 # Get a 128 byte key
            ) 
    return hash_new_password

def get_number_of_pages_from_search(report):
    print("function called")
    number_of_reports = report.count()
    page_size = 10
    numOfPages = number_of_reports/page_size
    numOfPagesRounded = math.ceil(numOfPages)
    print(numOfPages)
    print(numOfPagesRounded)
    return numOfPagesRounded

def calculate_percentage_of_report_in_db(report, totalReportsCount):
    print("calculate_percentage reached")
    number_of_reports = report.count()
    print(number_of_reports)
    if number_of_reports == 0:
        percentageOfDb = "0"
    else:
        calculatePercentageDb = (number_of_reports/totalReportsCount)*100
        percentageOfDb = round(calculatePercentageDb)
    return percentageOfDb

def calculate_percentage_of_search_reported_to_authorities(report, reportedReportsCount):
    print("calculate_percentage reached for reported")
    number_of_reports = report.count()
    if number_of_reports == 0:
        reportedReports = "0"
    else:
        reportedReportsPercentage = (reportedReportsCount/number_of_reports)*100
        reportedReports = round(reportedReportsPercentage)
    return reportedReports

##########################################
# Routes


# Initial home page
@app.route('/')
@app.route('/homepage')
def homepage():
    report=mongo.db.report.find().count()
    user = session.get("email")
    print(user)
    return render_template("home.html", report=report)

@app.route('/developer')
def developer():
    session["email"] = "developer"
    session["name"] = "developer"
    return redirect(url_for("homepage"))

######################################################################
# User controls


#signup
@app.route('/signup')
def signup():
    list_existing_emails = []
    used_email = mongo.db.user_credentials.find()
    print(used_email)
    for x in used_email:
        print(x["user_email"])
        list_existing_emails.append(x["user_email"])
        print(list_existing_emails)
    return render_template("signup.html", list_existing_emails=list_existing_emails)

#signup
@app.route('/creating_user', methods=['POST'])
def creating_user():
    salt = os.urandom(32)
    new_username= request.form['new_username']
    print(new_username)
    new_password = request.form['new_password']
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,new_username)):  
        print("Valid Email")  
        
        check_username_availibility = mongo.db.user_credentials.find_one({"user_email": new_username})
        print(check_username_availibility)
        if check_username_availibility == None:
            flag = is_new_password_valid(new_password) 
            print(flag)       
            if flag ==-1: 
                print("Not a Valid Password")
                flash('Please use a valid password')
                return redirect(url_for('signup'))
            
            hash_new_password = hashing_a_new_password(new_password, salt)
            
            mongo.db.user_credentials.insert_one({"user_email": new_username, "user_password": hash_new_password, "salt": salt})
            session["email"] = new_username
            return render_template("preferredName.html")
        else:
            return redirect(url_for('signup'))
    else:  
        flash('Please use a valid email format. For example - email@test.com')
        return redirect(url_for('signup'))


@app.route('/insert_name', methods=['POST'])
def insert_name():
    currentUserEmail = session.get("email")
    preferred_name = request.form['preferredNameInput'].lower()
    session["name"] = preferred_name
    mongo.db.user_credentials.update_one({"user_email": currentUserEmail},{"$set": {"name": preferred_name}})
    return redirect(url_for('dashboard'))

######################################################################

#login page
@app.route('/login')
def login():
    return render_template("login.html")


    
@app.route('/check_password', methods=['POST'])
def check_password():
    login_email = request.form['login_username']  
    login_password = request.form['login_password']
    print(login_password)
    current_user = mongo.db.user_credentials.find_one({"user_email": login_email})
    stored_password = get_user_password(current_user)
    stored_salt = get_user_password_salt(current_user)
    login_name = get_user_login_name(current_user)
    hash_login_password = hash_a_password_to_check_it_is_correct(stored_salt, login_password)
    print(hash_login_password)
    if stored_password == hash_login_password:
        print("match")
        session["email"] = login_email
        username = session.get("email")
        session["name"] = login_name              
        return redirect(url_for('dashboard'))
    else:
        print("no match")
        return render_template('login.html')


############################################################
# Dashboard


#dashboard
@app.route('/dashboard')
def dashboard():
    if session.get("email") is None:
        flash('Please login to see all of our amazing features')
        return redirect(url_for('login'))
    else: 
        user = session.get("email")
        print(user)
        userName = session.get("name")
        total=mongo.db.report.find({"email": user}).count()
        category = mongo.db.report.find({"email": user}).distinct("category_name")
        building = mongo.db.report.find({"email": user}).distinct("building")
        city = mongo.db.report.find({"email": user}).distinct("city")
        county = mongo.db.report.find({"email": user}).distinct("county")
        postcode = mongo.db.report.find({"email": user}).distinct("postcode")        
        return render_template('user_dash.html', name=userName, categories=mongo.db.categories.find(),
                               currentUserEmail=user, postcode=postcode, city=city, county=county, building=building, category=category, total=total)


#####################################################

# User preferences


@app.route('/userSetting')
def userSetting():
    if session.get("email") is None:
        flash('Please login to see all of our amazing features')
        return redirect(url_for('login'))
    else:
        user_email = session.get('email')
        current_user = mongo.db.user_credentials.find_one({"user_email": user_email}) 
        user_password = get_user_password(current_user)   
        preferred_name = session.get('name')    
        return render_template("settings.html", user_email=user_email, user_password=user_password, preferred_name=preferred_name)


@app.route('/changeDetails', methods=['POST'])
def changeDetails():
    if session.get("email") is None:
        flash('Please login to see all of our amazing features')
        return redirect(url_for('login'))
    else:   
        changeType = request.form['changeType']
        currentEmail = session.get("email")
        if changeType == 'password':
            salt = os.urandom(32)
            # Validating the new password
            new_password = request.form['updatePassword']
            flag = is_new_password_valid(new_password)
            print("This is the flag")
            print(flag)
            if flag ==-1: 
                print("Not a Valid Password")
                flash('Please use a valid password')
                return redirect(url_for('userSetting'))

            # Hashing the new password ready for the database
            
            print(new_password)
                      

            # Checking the current password is correct.
            current_user = mongo.db.user_credentials.find_one({"user_email": currentEmail})
            stored_password = get_user_password(current_user)
            stored_salt = get_user_password_salt(current_user)
            login_password = request.form['confirmCurrentPass']
            hash_new_password = hashing_a_new_password(new_password, salt)
            hash_login_password = hash_a_password_to_check_it_is_correct(stored_salt, login_password)
            if hash_login_password == stored_password:
                mongo.db.user_credentials.update_one({"user_email": currentEmail},{"$set": {"user_password": hash_new_password, "salt": salt}})
                flash("Password updated")
                return redirect(url_for('userSetting'))

            else: 
                flash("Incorrect password")
                return redirect(url_for('userSetting'))




        if changeType == 'email':
            
            print(currentEmail)
            updated_email = request.form['updateEmail']
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if(re.search(regex,updated_email)):  
                print("Valid Email")  
                
                check_username_availibility = mongo.db.user_credentials.find_one({"user_email": updated_email})
                print(check_username_availibility)
                if check_username_availibility == None: 
                    mongo.db.user_credentials.update_one({"user_email": currentEmail},{"$set": {"user_email": updated_email}})
                    mongo.db.report.update_many({"email": currentEmail},{"$set": {"email": updated_email}})
                    flash("Email updated.")
                    session.pop("email", None)
                    session["email"] = updated_email
                    return redirect(url_for('userSetting'))
                else:
                    flash("Sorry, that email is taken.")
                    return redirect(url_for('userSetting'))
            else: 
                flash("Please use a valid email.")
                return redirect(url_for('userSetting'))
        if changeType == 'name':
            updated_name = request.form['updateName']
            mongo.db.user_credentials.update_one({"user_email": currentEmail},{"$set": {"name": updated_name}})
            flash("Name updated.") 
            session.pop("name", None)  
            session["name"] = updated_name    
            return redirect(url_for('userSetting'))
    


@app.route('/delete_user', methods=['POST'])
def delete_user():
    if session.get("email") is None:
        flash('Please login to see all of our amazing features')
        return redirect(url_for('login'))
    else:
        current_user = session.get('email')
        login_password = request.form['deletePassword']
        
        user = mongo.db.user_credentials.find_one({"user_email": current_user})
        stored_salt = get_user_password_salt(current_user)
        user_password = get_user_password(current_user)
        hash_login_password = hash_a_password_to_check_it_is_correct(stored_salt, login_password)
        if hash_login_password == user_password:
            mongo.db.user_credentials.delete_one({"user_email": current_user})
            flash('We are sorry to see you go, but come back any time!')
            session.pop("email", None)
            session.pop("name", None)
            return redirect(url_for('signup'))
        else:
            flash('Password incorrect')
            return redirect(url_for('dashboard'))
                

###################################################################
# Logout

@app.route('/logout')
def logout():
    session.pop("email", None)
    session.pop("name", None)
    return redirect(url_for('homepage'))
  
    


##############################################

# Reading reports



# current working
@app.route('/search_reports', methods=['GET', 'POST'])
def search_reports():
    typeOfSearch = request.form['userSearchOwnReports']
    user_email = session.get("email")
    totalReportsCount = mongo.db.report.find().count()
    if typeOfSearch == "all":
        print("see All")
        report = mongo.db.report.find({"email": user_email})
        number_of_reports = report.count()
        searchingUserDb = "yes"
        page_size = 10
        numOfPagesRounded = get_number_of_pages_from_search(report)
        pages = []
        page1 = mongo.db.report.find({"email": user_email}).limit(page_size)
        pages.append(page1)
        for x in range(numOfPagesRounded):
            page = mongo.db.report.find({"email": user_email}).skip(int(x+1)*10).limit(page_size)
            pages.append(page)
        return render_template('userSearchResult.html', searchingUserDb=searchingUserDb, number_of_reports=number_of_reports, collapsibles=numOfPagesRounded, pages=pages)
        


    elif typeOfSearch == "location":
        print("see location")
        locationType = request.form['locationType']
        print(locationType)
        if locationType == 'building':
            building_name = request.form['building']
            print(building_name)
            extraLocation = request.form['extraLocationSearchWithBuilding']
            print(extraLocation)
            if extraLocation == "all":
                report = mongo.db.report.find( { "$and": [ {"email": user_email}, { "building":building_name } ] } )
                number_of_reports = report.count()
                searchingUserDb = "yes"
                
                page_size = 10
                numOfPagesRounded = get_number_of_pages_from_search(report)
                pages = []
                page1 = mongo.db.report.find( { "$and": [ {"email": user_email}, { "building":building_name } ] } ).limit(page_size)
                pages.append(page1)
                for x in range(numOfPagesRounded):
                    page = mongo.db.report.find( { "$and": [ {"email": user_email}, { "building":building_name } ] } ).skip(int(x+1)*10).limit(page_size)
                    pages.append(page)
                return render_template('userSearchResult.html', number_of_reports=number_of_reports, searchingUserDb=searchingUserDb, report=report, collapsibles=numOfPagesRounded, pages=pages)
            else:
                extraLocationValue = request.form[extraLocation]        
                report = mongo.db.report.find( { "$and": [ {"email": user_email}, { "building":building_name }, { extraLocation : extraLocationValue} ] } )
                number_of_reports = report.count()
                searchingUserDb = "yes"
                
                page_size = 10
                numOfPagesRounded = get_number_of_pages_from_search(report)
                pages = []
                page1 = mongo.db.report.find( { "$and": [ {"email": user_email}, { "building":building_name }, { extraLocation : extraLocationValue} ] } ).limit(page_size)
                pages.append(page1)
                for x in range(numOfPagesRounded):
                    page = mongo.db.report.find( { "$and": [ {"email": user_email}, { "building":building_name }, { extraLocation : extraLocationValue} ] } ).skip(int(x+1)*10).limit(page_size)
                    pages.append(page)
                return render_template('userSearchResult.html', number_of_reports=number_of_reports, searchingUserDb=searchingUserDb, report=report, collapsibles=numOfPagesRounded, pages=pages)
        else:
            value = request.form[locationType]
            report = mongo.db.report.find( { "$and": [ {"email": user_email}, { locationType : value } ] } )
            number_of_reports = report.count()
            searchingUserDb = "yes"
            page_size = 10
            
            numOfPagesRounded = get_number_of_pages_from_search(report)
            pages = []
            page1 = mongo.db.report.find( { "$and": [ {"email": user_email}, { locationType : value } ] } ).limit(page_size)
            pages.append(page1)
            for x in range(numOfPagesRounded):
                page = mongo.db.report.find( { "$and": [ {"email": user_email}, { locationType : value } ] } ).skip(int(x+1)*10).limit(page_size)
                pages.append(page)
            return render_template('userSearchResult.html', searchingUserDb=searchingUserDb, number_of_reports = number_of_reports, report=report, collapsibles=numOfPagesRounded, pages=pages)

    elif typeOfSearch == "date":
        print("see date")
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        report = mongo.db.report.find( { "$and": [ {"email": user_email}, {"date":{ "$gte": startDate,"$lt":endDate }}  ] } )
        print(report)
        number_of_reports = report.count()
        searchingUserDb = "yes"
        page_size = 10
        
        pages = []
        page1 = mongo.db.report.find( { "$and": [ {"email": user_email}, {"date":{ "$gte": startDate,"$lt":endDate }}  ] } ).limit(page_size)
        pages.append(page1)
        for x in range(numOfPagesRounded):
            page = mongo.db.report.find( { "$and": [ {"email": user_email}, {"date":{ "$gte": startDate,"$lt":endDate }}  ] } ).skip(int(x+1)*10).limit(page_size)
            pages.append(page)
        return render_template('userSearchResult.html', searchingUserDb=searchingUserDb, number_of_reports=number_of_reports, report=report, collapsibles=numOfPagesRounded, pages=pages)
    else:
        print("see discrimin")
        category = request.form['category']
        print(category)
        report = mongo.db.report.find( { "$and": [ {"email": user_email}, { "category_name":category } ] } ) 
        number_of_reports = report.count()
        searchingUserDb = "yes"
        page_size = 10
        numOfPagesRounded = get_number_of_pages_from_search(report)      
        pages = []
        page1 = mongo.db.report.find( { "$and": [ {"email": user_email}, { "category_name":category } ] } ).limit(page_size)
        pages.append(page1)
        for x in range(numOfPagesRounded):
            page = mongo.db.report.find( { "$and": [ {"email": user_email}, { "category_name":category } ] } ).skip(int(x+1)*10).limit(page_size)
            pages.append(page)
        return render_template('userSearchResult.html', searchingUserDb=searchingUserDb, number_of_reports=number_of_reports, report=report, collapsibles=numOfPagesRounded, pages=pages)

#####################################################

@app.route('/search_db_reports', methods=['GET', 'POST'])
def search_db_reports():
    totalReportsCount = mongo.db.report.find().count()
    typeOfSearch = request.form['userSearchReports']
    # Search entire db
    if typeOfSearch == "searchAll":
        useTimeFrame = request.form['useTimeFrame']
        print(useTimeFrame)
        if useTimeFrame == "No":
            print("see All")
            report = mongo.db.report.find()
            reportedReportsCount = mongo.db.report.find({"report_to_authorities": "Yes"}).count()
        else:
            # Search entire db with time frame
            startDate = request.form['allStartDateFrame']
            print(startDate)
            endDate = request.form['allEndDateFrame']
            print(endDate)
            report = mongo.db.report.find({"date":{ "$gte": startDate,"$lt":endDate }})
            reportedReportsCount = mongo.db.report.find( {"$and":[{"date":{ "$gte": startDate,"$lt":endDate }}, {"report_to_authorities": "Yes"}] }).count()
        number_of_reports = report.count()
        # Statistics for the top of the search page.
        percentageOfDb = calculate_percentage_of_report_in_db(report, totalReportsCount)
        numOfPagesRounded = get_number_of_pages_from_search(report)      
        reportedReports = calculate_percentage_of_search_reported_to_authorities(report, reportedReportsCount) 
        # Pagination
        pages = []
        page_size = 10
        page1 = mongo.db.report.find().limit(page_size)
        pages.append(page1)
        for x in range(numOfPagesRounded):
            page = mongo.db.report.find().skip(int(x+1)*10).limit(page_size)
            pages.append(page)
        return render_template('userSearchResult.html', percentageOfDb=percentageOfDb, reportedReports=reportedReports, number_of_reports=number_of_reports, report=report, collapsibles=numOfPagesRounded, pages=pages)

    # Search db by Location
    elif typeOfSearch == "searchByLocation":
        print("see location")
        locationType = request.form['locationType']
        print(locationType)
        # Search by building
        if locationType == 'building':
            building_name = request.form['building']
            print(building_name)
            extraLocation = request.form['extraLocationSearchWithBuilding']
            print(extraLocation)
            if extraLocation == "all":
                # Search buildings in all locations with no time frame
                useTimeFrame = request.form['useTimeFrame']
                if useTimeFrame == "No":
                    print("see All")
                    report = mongo.db.report.find( {"building":building_name } )
                    reportedReportsCount = mongo.db.report.find( {"$and":[{"building":building_name }, {"report_to_authorities": "Yes"}] }).count()
                else:
                    # Search buildings in all locations with time frame
                    startDate = request.form['StartDateLocation']
                    print(startDate)
                    endDate = request.form['allEndDateLocation']
                    print(endDate)
                    report = mongo.db.report.find({"$and": [{"building":building_name }, {"date":{ "$gte": startDate,"$lt":endDate }}]})                
                    reportedReportsCount = mongo.db.report.find( {"$and":[{"building":building_name }, {"date":{ "$gte": startDate,"$lt":endDate }}, {"report_to_authorities": "Yes"}] }).count()
                # Statistics for results page
                page_size = 10
                number_of_reports = report.count()
                percentageOfDb = calculate_percentage_of_report_in_db(report, totalReportsCount)
                    
                reportedReports = calculate_percentage_of_search_reported_to_authorities(report, reportedReportsCount)        
                # Pagination
                numOfPagesRounded = get_number_of_pages_from_search(report)
                pages = []
                page1 = mongo.db.report.find( {"building":building_name } ).limit(page_size)
                pages.append(page1)
                for x in range(numOfPagesRounded):
                    page = mongo.db.report.find( {"building":building_name } ).skip(int(x+1)*10).limit(page_size)
                    pages.append(page)
                return render_template('userSearchResult.html', percentageOfDb=percentageOfDb, number_of_reports=number_of_reports, reportedReports=reportedReports, report=report, collapsibles=numOfPagesRounded, pages=pages)
            else:
                extraLocationValue = request.form[extraLocation]   
                useTimeFrame = request.form['useTimeFrame']
                if useTimeFrame == "No":
                    print("see All")
                    report = mongo.db.report.find( { "$and": [ {"building":building_name }, { extraLocation : extraLocationValue} ] } )
                    reportedReportsCount = mongo.db.report.find( {"$and":[{"building":building_name }, { extraLocation : extraLocationValue}, {"report_to_authorities": "Yes"}] }).count()
                else:
                    startDate = request.form['StartDateLocation']
                    print(startDate)
                    endDate = request.form['allEndDateLocation']
                    print(endDate)
                    report = mongo.db.report.find( { "$and": [ {"building":building_name }, { extraLocation : extraLocationValue},{"date":{ "$gte": startDate,"$lt":endDate }} ] } )
                    reportedReportsCount = mongo.db.report.find( {"$and":[{"building":building_name }, { extraLocation : extraLocationValue}, {"date":{ "$gte": startDate,"$lt":endDate }}, {"report_to_authorities": "Yes"}] }).count()
                # Statistics for search page
                number_of_reports = report.count()
                percentageOfDb = calculate_percentage_of_report_in_db(report, totalReportsCount) 
                reportedReports = calculate_percentage_of_search_reported_to_authorities(report, reportedReportsCount)        
                # Pagination
                numOfPagesRounded = get_number_of_pages_from_search(report)        
                page_size = 10
                pages = []
                page1 = mongo.db.report.find( { "$and": [ {"building":building_name }, { extraLocation : extraLocationValue} ] } ).limit(page_size)
                pages.append(page1)
                for x in range(numOfPagesRounded):
                    page = mongo.db.report.find( { "$and": [ {"building":building_name }, { extraLocation : extraLocationValue} ] } ).skip(int(x+1)*10).limit(page_size)
                    pages.append(page)
                return render_template('userSearchResult.html', number_of_reports=number_of_reports, percentageOfDb=percentageOfDb, reportedReports=reportedReports, report=report, collapsibles=numOfPagesRounded, pages=pages)
        else:
            if locationType == 'city':
                value = request.form['city']  
            elif locationType == 'county':
                value = request.form['county']    
            else:
                value = request.form['postcode']
            useTimeFrame = request.form['useTimeFrame']
            print(useTimeFrame)
            if useTimeFrame == "No":
                print("see All")
                report = mongo.db.report.find( {locationType:value } )
                reportedReportsCount = mongo.db.report.find( {"$and":[{locationType:value }, {"report_to_authorities": "Yes"}] }).count()
            else:
                startDate = request.form['startDateLocation']
                print(startDate)
                endDate = request.form['endDateLocation']
                print(endDate)
                report = mongo.db.report.find( {"$and":[{locationType:value }, {"date":{ "$gte": startDate,"$lt":endDate }}]})           
                reportedReportsCount = mongo.db.report.find( {"$and":[{locationType:value }, {"date":{ "$gte": startDate,"$lt":endDate }}, {"report_to_authorities": "Yes"}] }).count()
            # Statistics for search results pages
            number_of_reports = report.count()
            percentageOfDb = calculate_percentage_of_report_in_db(report, totalReportsCount) 
            reportedReports = calculate_percentage_of_search_reported_to_authorities(report, reportedReportsCount)        
             # Pagination
            numOfPagesRounded = get_number_of_pages_from_search(report)        
           
            page_size = 10
            pages = []
            page1 = mongo.db.report.find( {locationType:value } ).limit(page_size)
            pages.append(page1)
            for x in range(numOfPagesRounded):
                page = mongo.db.report.find( {locationType:value } ).skip(int(x+1)*10).limit(page_size)
                pages.append(page)
                print(pages)
            return render_template('userSearchResult.html', reportedReports=reportedReports, percentageOfDb=percentageOfDb, number_of_reports=number_of_reports, report=report, collapsibles=numOfPagesRounded, pages=pages)              
              

    elif typeOfSearch == "searchByDiscrimination":
        print("see discrimin")
        category = request.form['category']
        useTimeFrame = request.form['useTimeFrame']
        print(useTimeFrame)
        if useTimeFrame == "No":
            print("see All")
            report = mongo.db.report.find( { "category_name":category } )
            reportedReportsCount = mongo.db.report.find( {"$and":[{ "category_name":category }, {"report_to_authorities": "Yes"}] }).count()
        else:
            startDate = request.form['categoryStartDateFrame']
            print(startDate)
            endDate = request.form['categoryEndDateFrame']
            print(endDate)
            report = mongo.db.report.find( {"$and":[{ "category_name":category }, {"date":{ "$gte": startDate,"$lte":endDate }}]}) 
            reportedReportsCount = mongo.db.report.find( {"$and":[{ "category_name":category }, {"report_to_authorities": "Yes"}, {"date":{ "$gte": startDate,"$lte":endDate }}]}).count()           
        # Statistics
        number_of_reports = report.count()
        percentageOfDb = calculate_percentage_of_report_in_db(report, totalReportsCount)
        reportedReports = calculate_percentage_of_search_reported_to_authorities(report, reportedReportsCount)
        # Pagination
        page_size = 10
        numOfPagesRounded = get_number_of_pages_from_search(report)        
        pages = []
        page1 = mongo.db.report.find( { "category_name":category }).limit(page_size)
        pages.append(page1)
        for x in range(numOfPagesRounded):
            page = mongo.db.report.find( { "category_name":category }).skip(int(x+1)*10).limit(page_size)
            pages.append(page)
        return render_template('userSearchResult.html', number_of_reports=number_of_reports, reportedReports=reportedReports, percentageOfDb=percentageOfDb, report=report, collapsibles=numOfPagesRounded, pages=pages)
    else:
        print("see reported")
        reportedToAuthorities = request.form['searchReported']
        useTimeFrame = request.form['useTimeFrame']
        print(useTimeFrame)
        if useTimeFrame == "No":
            print("see All")
            report = mongo.db.report.find({"report_to_authorities": reportedToAuthorities }  )
            reportedReportsCount = mongo.db.report.find( {"$and":[{"report_to_authorities": reportedToAuthorities }, {"report_to_authorities": "Yes"}]}).count() 
        else:
            startDate = request.form['reportedStartDateFrame']
            print(startDate)
            endDate = request.form['reportedEndDateFrame']
            print(endDate)
            report = mongo.db.report.find( {"$and":[{"report_to_authorities": reportedToAuthorities } , {"date":{ "$gte": startDate,"$lt":endDate }}]})           
            reportedReportsCount = mongo.db.report.find( {"$and":[{"report_to_authorities": reportedToAuthorities }, {"report_to_authorities": "Yes"}, {"date":{ "$gte": startDate,"$lte":endDate }}]}).count()           
        
        print(report)
        # Statistics 
        number_of_reports = report.count()
        percentageOfDb = calculate_percentage_of_report_in_db(report, totalReportsCount)
        reportedReports = calculate_percentage_of_search_reported_to_authorities(report, reportedReportsCount)
        # Pagination
        numOfPagesRounded = get_number_of_pages_from_search(report)  
        page_size = 10
        
        pages = []
        page1 = mongo.db.report.find(  {"report_to_authorities": reportedToAuthorities } ).limit(page_size)
        pages.append(page1)
        for x in range(numOfPagesRounded):
            page = mongo.db.report.find(  {"report_to_authorities": reportedToAuthorities } ).skip(int(x+1)*10).limit(page_size)
            pages.append(page)
        return render_template('userSearchResult.html', reportedReports=reportedReports, percentageOfDb=percentageOfDb, number_of_reports=number_of_reports, report=report, collapsibles=numOfPagesRounded, pages=pages)



@app.route('/get_report')
def get_report():
    return render_template("report.html", report=mongo.db.report.find())    


# This is the OG screen with one search box as default.
@app.route('/search_report')
def search_report():
    total = mongo.db.report.find().count()
    category = mongo.db.report.find().distinct("category_name")
    building = mongo.db.report.find().distinct("building")
    city = mongo.db.report.find().distinct("city")
    county = mongo.db.report.find().distinct("county")
    postcode = mongo.db.report.find().distinct("postcode")        
    return render_template('searchResults.html', categories=mongo.db.categories.find(),
                            postcode=postcode, city=city, county=county, building=building, category=category, total=total) 


#######################################################################
# Creating reports

@app.route('/add_report')
def add_report():
    currentUserEmail = session.get("email")
    if currentUserEmail == None:
        currentUserEmail = "anonymous"
        print(currentUserEmail)
        return render_template("add_report.html", currentUserEmail=currentUserEmail, categories=mongo.db.categories.find(),
                           
                           )
    else:
        return render_template("add_report.html", currentUserEmail=currentUserEmail, categories=mongo.db.categories.find(),
                           
                           )

@app.route('/insert_report', methods=['GET','POST'])
def insert_report():
    report = mongo.db.report
    report.insert_one(request.form.to_dict())
    print(report)
    if session.get("email") is None:
        return redirect(url_for('add_report'))
    else:
        return redirect(url_for('dashboard'))


#####################################################################################
# Updating reports
@app.route('/user_modify/<report_id>')
def user_modify(report_id):
    the_report = mongo.db.report.find_one({"_id": ObjectId(report_id)})
    print(the_report)
    available_categories = mongo.db.categories.find()
    
    currentUserEmail = session.get("email")
    return render_template('user_modify.html', currentUserEmail=currentUserEmail, report=the_report, categories=available_categories)

@app.route('/edit_report/<report_id>', methods=["POST"])
def edit_report(report_id):
    print("accessed")
    report = mongo.db.report
    report.update({'_id': ObjectId(report_id)},
                  {
                  'email': request.form.get('email'),
                  'username': request.form.get('username'),
                  'category_name': request.form.get('category_name'),
                  'incident_description': request.form.get('incident_description'),
                  'building': request.form.get('building'),
                  'street': request.form.get('street'),
                  'city': request.form.get('city'),
                  'county': request.form.get('county'),
                  'postcode': request.form.get('postcode'),
                  'report_to_authorities': request.form.get('report_to_authorities')
                  })
    return redirect(url_for('dashboard'))

##################################################################
# Deleting reports

@app.route('/confirm_delete_report/<report_id>')
def confirm_delete_report(report_id):
    the_report = mongo.db.report.find_one({"_id": ObjectId(report_id)})
    ###################### Check this is needed?
    available_categories = mongo.db.categories.find()
    

    return render_template('confirm_delete.html', report=the_report, categories=available_categories)


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