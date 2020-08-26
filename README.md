# Report On Any Discrimination

![Image a website on different devices](static/files/wireframes/responsive-design.jpg)

### [Live page](https://ms3-cgpalmer91.herokuapp.com/)

# Disclaimer

The statistics on this website are free to use. However, they must be reported responsibly and with context. 

Any misrepresentation of the statistics will be denounced and asked to remove them. 

Please do not use a person's name in the reports, as the report will be removed.



___

## Contents
+ <a href="#rationale">Rationale</a>
    - <a href="#inspiration">Inspiration</a>
+ <a href="#UX">UX</a> 
   - <a href="#userStories">User Stories</a>
+ <a href="#features">Features</a>
   - <a href="#existingFeatures">Existing Features</a>
   - <a href="#featuresLeftToImplement">Features left To Implement</a>
+ <a href="#defensiveFeatures">Defensive Features</a>
+ <a href="#technologiesUsed">Technologies Used</a>
+ <a href="#testing">Testing</a>
+ <a href="#responsiveDesign">Responsive design</a>
+ <a href="#deployment">Deployment</a>
   - <a href="#deploymentLive">Deployment Live</a>
   - <a href="#deploymentLive">Deployment Local</a>
+ <a href="#credit">Credit</a>
   - <a href="#tutorials">Tutorials</a>
   - <a href="#media">Media</a>
   - <a href="#acknowledgements">Acknowledgements</a>
+ <a href="#project">Project Evaluation</a>
   - <a href="#improvements">Improvements</a>






___

<span id="rationale"></span>
## Rationale

## Project proposal

The project aim to create a database of discrimination across the UK. It will allow users to take a stand and 
report any discrimination they experience, hear or see. They can categorise the discrimination and add a location.

This project will be open-sourced and all councils, police, charities and authories will have access to the data.
They can search by area or by discrimination to see where they can focus their efforts and funding.

___

<span id="inspiration"></span>

## Inspiration

#### Requesting information

I designed this website to be as intuative and quick as possible. A major factor for not recording events is simply 
the amount of time it can take out of the day. Therefore, I designed my web site to only request the information
it necessary. 

I read an article explaining how to create a minimalist registering page at this link:
https://www.smashingmagazine.com/2011/05/innovative-techniques-to-simplify-signups-and-logins/

Using it as inspiration, I simplified my registering form and allowed user to sign up as quickly as possible.
I also allowed them to add a preferred name once they were signed up, again speeding up the process.

I took this a step further with adding a new report or searching for a report. 

When adding a report, you are required to give information on whether the incident has been reported, 
the category of the incident and a description. As soon as that information was supplied, the incident was recorded.
After that, the user had the option to add extra details such as date and location. This offers flexibility to the
user and encourages use even if all the details aren't accessible.

When searching for a report, you only need to select the information necessary for your search. Otherwise, the Javascript
hides the extra information.

#### Design

I wanted this website to have a calm and mature theme - one that matches and reflects the sombre but important purpose.
In order to do this, I looked at two particular design websites that are linked below:
https://visme.co/blog/color-combinations/?fbclid=IwAR04pjyYtd1uGzsv9jQWIOkG3KCayjX2nGdH6xTy9WPapcLV0Xie3HKmWg0
https://visme.co/blog/website-color-schemes/?fbclid=IwAR16fr1TqIOxw-Juvp4z_FFiHoHpONwH6D6g7Eud2-aVdneS0q2DHFfTWPg

I finally decided on one that had earth tones, which promoted calm and clarity. I attempted where possible to stick 
to as few colour as possible and ensured they complimented each other. 

___

<span id="UX"></span>
## UX

<span id="userStories"></span> 
### User Stories

#### First-time user
1. As a first-time user, I want to easily navigate through the website be able to easily access all of its features.
2. As a first-time user, I want to be able to immediately see what the website is about.
3. As a first-time user, I want to be able to create an account.
4. As a first-time user, I want to be able to log in with my new account.
5. As a first time user, I want to be able to explore the dashboard immediately.
6. As a first time user, I want to be able to add a report regardless of whether I have created an account or not.
7. As a first-time user, I want to be able to search reports. 
8. As a first-time user, I want to be able to log out when I am done.
9. As a first-time user, I want my personal details to be private and kept away from the reports.  

#### Returning user

1. As a returning user, I want to be able to log in easily.
2. As a As a returning user, I want to be able to do all the things as stated in a new user with the same ease.
3. As a returning user, I want to search through my own reports.
4. As a returning user, I want to be able to add a report and it go into my collection.
5. As a returning user, I want to be able to modify one of my reports.
6. As a returning user, I want to be able to delete one of my reports.
7. As a returning user, I want to be able to change my preferred name.
8. As a returning user, I want to be able to change my email.
9. As a returning user, I want to be able to change my password.
10. As a returning user, I want to be able to delete my account.

#### User as a charity or researcher (professional user)

1. As a profession user, I want to be able to see some statistics about my search so I can compare them to other searches.

### Wireframes

Wireframes have been made using Balsamiq. 

[Wireframes](static/files/wireframes/ms3-wireframes-with-notes.pdf)

As there were not initial wireframes of the all the screen, I have added responsive images of all the pages in their final form.
[- responsive images of actual site.](static/files/wireframes/responsive-images-instead-of-WF.pdf)
___
<span id="features"></span>
## Features

<span id="existingFeatures"></span>
### Existing Features

<ins>Navbar</ins>

1. The navbar is responsive and had a traditional 'hamburger' icon on devices smaller than a laptop.
2. Each link will take the user to the designated pages.
3. There are links for the home page, login page, signup page, add report, search report - initially.
4. When logged in the links change to the following: - home page, dashboard, logout, add report, search report.
5. The logo will take the user back to the home page.

<ins>Footer</ins>

1. An email address which the user can contact the team by.
2. A telephone which the users can contact the team by.

<ins>Home </ins>

1. There is an update on how many reports have been collected altogether.
2. User can see the purpose of the website clearly.
3. There is information about the team behind the website.
4. There is a disclaimer giving advice on how to use the website. 

<ins>Dashboard </ins>

1. Has a welcome message with the users name.
2. A collapsible gives the user the three options:- Manage their own reports, search the database or add a report.
3. The search our database and add report links will take the user to the designated pages for adding reports and 
   searching the database.
4. The managing reports part of the collapsible is open.
5. The user can search their own reports by searching all, by location or by discrimination.
6. Button is disabled until the right amount of information is given.
7. There is a settings button which will take the user to the settings.



<ins>Login </ins>

1. A form to input user details which will allow them to log in.
2. A button which will submit the form.
3. If the user inputs an incorrect email or password, then a message will flash underneath the heading giving 
   the user feedback.
4. There is advice on how a user can reset their password.
5. There is a link to the signup page in case the user doesn't yet have an account. 

<ins>Signup</ins>

1. A form to fill in in order to register an account.
2. A lightbulb will give the users information for the password requirements. 
3. There is an eye-icon which users can press to see the password they have inputted.
4. When the user enters a password that meets the criteria a tick will be displayed next to the eye-icon.
5. There is a check button the user must click to confirm they have checked the password.
6. Once signed up, the user is redirected to another page where they can enter their preferred name.

<ins>Add report</ins>

1. There is a reminder to not use person's name in the report.
2. There are initial options to start the report.
3. There is a disabled button which will become enabled when all the options have been chosen.
4. Upon pushing the add report button, the user is taken to a new screen where they can add a loction or skip 
   and then add a date.  

<ins>Search report</ins>

1. There collapsible from materialize that has four options: Search by discrimination, location, whether it has been reported or all.
2. If the user clicks on a header, then that part of the collapsible stands out to draw focus. 
3. In all search options except 'search all', there is an option to choose a date frame within which to search.
4. For the discrimination option, you can choose from the pre-selected discrimination categories. 
5. For the location option, you can choose any of the pre-set location options.
6. Should you choose to search by buildings, you may choose a second location in order to compare. 
7. Like in the add report, the button stays disabled until the user has given enough information for a viable report.
8. Starred inputs are there to show the user which information is needed.
9. For searching by reported to authorities, there is a choice between whether the report has or hasn't been reported.

<ins>Settings</ins>

1. There is a collapsible on the settings page where the user can change name, password, email or delete account.
2. Each of the options above are in their own collapsible body.
3. The current name, password, email have the original values displayed underneath.
4. When deleting the account, the user must put in their correct password.  

<ins>Search Result</ins>

1. All results are within a card and display all of the report information.
2. The pagination works by splitting up the reports ten at a time and putting them in separate collapsibles.
3. At the top of the page, the user will get three statistics: How many reports, what percentage they make up of 
   the database they make, and how many have been reported to authorities. 
4. There are two choices with each report: to either edit or delete the report.


<ins>User Modify</ins>

1. The user modify page has a form with all previous values form the report.
2. The user can modify any of the values and resubmit the form.

<ins>User Delete</ins>

1. The user delete page will show a single report with a delete button.

<span id="featuresLeftToImplement"></span>
### Features Left to Implement

- The date will present itself the correct way round.
- Automatic email will be sent to the website managers when a report is updated/added
- Public can recommend categorise when adding a report rather than having to email separately.
- A google api will allow the locations of the features to be displayed as clusters across a map. 
- People can filter incidents just by a date frame. 
- Export data as a CSV to be used on excel.
- Councils/ other professional bodies will be able to upload reports of discrimination via their own CSV.


___
<span id="defensiveFeatures"></span>
## Defensive Features

+ I wanted to make sure that the users inputted all the information necessary for a successful search. 
  So I have used JS to disable the buttons until a criteria has been met. 
+ If you try to access any of the web pages that are reserved for account holders, it will redirect you to the login
  page. I did this to help protect people's reports so that only they could modify them. 
+ A new user cannot use the same email as a current user. This is because the functionality of the website uses the
  email address to identify which user to assign the report to. 
+ I ask the user to confirm their password before they can delete their account.
+ The passwords are hashed and a different salt is generated each time a password is made/changed. If anyone hacks into
  database they will not be able to see the passwords.

___
<span id="technologiesUsed"></span>
### Technologies Used

Languages used

1. HTML
2. CSS
3. Javascript
4. Python 

Frameworks

1. Materialize 1.0.0
2. Flask 
3. Jinja 
4. jQuery

___
<span id="testing"></span>

## Testing

 
### User stories

### General testing

### Responsive design

### Cross browser test

I have test my site on Microsoft Edge, Firefox and Chrome web browsers.
I specifically test the following things:
   + Do the collapsibles and their animations open?
   + Does the checkbox still work?
   + Does the tooltip work on the signup page?
   + Do the select options work? 

On the browsers Firefox, Edge and Chrome, all of th elements above are working properly.
I have attached a pdf of the results of the tests. They are only for Firefox and Edge as Chrome was my main developer and is
covered by my other testing.

[Firefox cross browser testing.](static/files/testing/crossBrowserTesting/crossBrowserFirefoxTest.pdf) 
[Edge cross browser testing.](static/files/testing/crossBrowserTesting/crossBrowserEdgeTest.pdf) 



### Code validation

#### Python
To check my python code validation, I have used a combination of 'cornflakes-linter 0.4.0' and http://pep8online.com/checkresult
I have configured the cornflakes to accept a line length of 120 characters.
Therefore, the only code issue that comes up on http://pep8online.com/checkresult is that the lines are too long as it is set to 79 characters.

#### CSS
CSS has been checked by this online validator: https://jigsaw.w3.org/css-validator/#validate_by_input
My css only has warnings about webkits being 'unknown vendor extensions'.
There are no issues with my css. 

#### HTML
My HTML has been checked on this website: https://validator.w3.org/

#### Javascript
My javascript has been checked at https://jshint.com/
There are no issues with my JS. 

### Interesting bugs

1. [Dividing by 0](static/files/testing/interesting-bugs-documentation/bug-for-dividing-by-0.pdf) 
2. [Logging in issues](static/files/testing/interesting-bugs-documentation/Issue-with-logging-in.pdf) 
3. [Console error breaking the JS flow](static/files/testing/interesting-bugs-documentation/js-console-error-interrupting-the-other-js.pdf) 
4. [Problems reading if the email address exists, live](static/files/testing/interesting-bugs-documentation/Live-reading-if-the-username-exists.pdf) 
5. [Only certain elements are being searched in the array](static/files/testing/interesting-bugs-documentation/Not-match-against-all-array-elements.pdf) 
6. [Problems with validating the password](static/files/testing/interesting-bugs-documentation/password-validation-issue.pdf) 





___
<span id="responsiveDesign"></span>
## Responsive Design

This project has been optimised to the common devices on Google Chrome's Dev Tools.
It has been specifically designed for the following:
   + Moto G4
   + iPhone 6/7/8
   + iPad
   + iPad Pro
   + Laptop with MDPI screen
   + Laptop with HiDPI screen


The majority of the website stays consistent to an easy user experience. There are minor changes to font-sizes etc. Some 
of these can be seen in the [responsive image](static/files/wireframes/responsive-design.jpg). This has been taken from the website:
http://ami.responsivedesign.is/#

There are a few major resposive choices, detailed below.

1. When viewing on a laptop the search results present their information in a different way. The incident description,
date and whether it had been reported are shown in their own colour on the right of the card.

2. The pictures of staff and descriptions shift to being alongside each other once on the laptop/ landscape iPad Pro 
screen.
___
<span id="deployment"></span>
## Deployment

<span id="deploymentLive"></span>
Deployment – Live Website  

   1.	Create repository in GitHub and give it a relevant name.
   

<span id="deploymentLocal"></span>
Deployment – Run Locally  

   1.	Again, click on the repository called The-Book-Club.
   


___
<span id="credit"></span>
## Credit

<span id="tutorials"></span>
<ins>Tutorials</ins>

For all of the following tutorials, I have edited the code necessary for my project. 

This tutorial helped me to make sure my urls were clearer.
https://restfulapi.net/resource-naming/

This tutorial helped me to alphabetise some areas of results.
https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2

This tutorial helped me to use the date-time function in python
https://www.dataquest.io/blog/python-datetime-tutorial/

This tutorial helped me to save the date from the input into the mongoDB.
https://stackoverflow.com/questions/58160212/how-to-save-date-from-datepicker-into-database-in-sqlalchemy-flask-application

This tutorial helped me to validate a password live for when users are deciding their first password.
https://www.w3resource.com/javascript/form/password-validation.php


This link helped to set up Flash-messages.
https://www.youtube.com/watch?v=DFCKWhoiHZ4

This tutorial helped me to store things to the Flask session.
https://pythonise.com/series/learning-flask/flask-session-object

This tutorial helped me to set up a back-end validation check which matched the live JS version.
https://www.geeksforgeeks.org/python-program-check-validity-password/


This tutorial helped me to check if there was a value in the array that matched the criteria.
https://stackoverflow.com/questions/55957237/checking-if-input-value-matches-the-array-items

This tutorial helped me to check the email live to see if there was already a user with that account.
https://stackoverflow.com/questions/14411235/while-typing-in-a-text-input-field-printing-the-content-typed-in-a-div

This link helped me to process a list of emails in python and access them in JS.
https://groups.google.com/forum/#!topic/web2py/OmwTo1ZsFN4

This link helped me to process a list from python into a json file.
https://stackoverflow.com/questions/23038710/accessing-python-list-in-javascript-as-an-array

This helped me to understand how I could get the value from a select option.
http://jsfiddle.net/YPsqQ/

Tutorial on how to hash a password
https://nitratine.net/blog/post/how-to-hash-passwords-in-python/


<span id="media"></span>
<ins>Media</ins>

To generate my favicon, I used this website: 

https://www.favicon.cc/



<span id="acknowledgements"></span>
<ins>Acknowledgements</ins>  

I used the Government's own website when choosing which categorise would be available. There are a few names I have
changed on the grounds that there are more colloquial terms available. Eg. 'Sex' has been changed to 'sexism'.
Please find the link attached below:
https://www.gov.uk/discrimination-your-rights


___
<span id="project"></span>
## Project Evaluation

I believe this website handles its purpose with maturity and simplicity. There is no unnecessary data collected and indeed
there is the option to skip it. The clean UX, complete with a responsive navbar, makes the site very easy to navigate.
All of the links to the user areas are in the same place and easy to access in the navbar. 
This is also complemented by a simple and complimentary colour scheme. They colours are calm and neutral which 
sets the correct tone for the purpose of the website.

There are a variety of way in which you can search through the reports. All of search options are on one webpage
which cuts down on screen loading time. In addition, elements of a form that aren't needed are hidden. Again, this
creates a clean user experience where the user is not over loaded with information.

Giving the user complete control over their own reports helps to promote trust in the website. Users can edit and
even delete their reports at any time. If a user is logged in they will be associated with that report in their dashboard
but no where else on the website. This allows flexibility and anonymity. 

Overall, I think the website has a clear purpose, clean UX and defensive features to ensure the user gets the most
out of the experience.



<span id="improvements"></span>
### Improvements

+ I would like to refactor the code that chooses whether you can search by a date.
+ The menu could have icons on it as a visual reminder.
+ There could be a dashboard button like the settings button on the pages as a shortcut.
+ I need to use an ajax to live check the email addresses when signing up as the regex will become slow and cumbersome 
  as the users grow.






___







