<h1 align="center">Shot Caller - Movie Production Website</h1>

[View the project live here.](https://ms3-shot-caller.herokuapp.com/)

A web application for film production that provides a reliable all encompassing
means of production collaboration from pre-production to post. The app is designed 
to provide a simple streamlined means of communication through the different 
departments channels of film production. It allows both a general and specific 
means on searching and uploading communications and images to different departments.

It has a secure admin facility for site regulation and the upkeep of the image
bank that includes a simple means of uploading the latest script, shotlist. The site 
is built with Flask using the Jinja template engine and the Werkzeug WSGI toolkit
and uses Mongodb as the back-end database.

Currently the app is limited to one production but future developements would
lead to it being turned into a piece of software that can be downloaded and used
as a product on an individual basis for each new production and owner.

<h2 align="center"><img src="documentation/readme-images/user16.png"></h2>

# Table of Content

- [User Experience (UX)](#user-experience--ux-)
  * [Strategy Plane](#strategy-plane)
  * [Scope Plane](#scope-plane)
  * [Structure Plane](#structure-plane)
  * [Skeleton Plane](#skeleton-plane)
  * [User stories](#user-stories)

- [Design](#design)

- [Existing Features](#existing-features)
  * [Responsive Design](#responsive-design)
  * [Login/Register Pages and Security Measures](#login-register-pages-and-security-measures)
  * [User Base Page](#user-base-page)
  * [Departments Page](#departments-page)
  * [Images Page](#images-page)
  * [Admin Page](#admin-page)

- [Database structure](#database-structure)

- [Languages Used](#languages-used)

- [Frameworks, Databases, Libraries & Programs Used](#frameworks--databases--libraries---programs-used)

- [Testing](#testing)

- [Lighthouse](#lighthouse)
  * [Login page](#login-page)
  * [Register page](#register-page)
  * [User Base page](#user-base-page)
  * [Image page](#image-page)
  * [Departments page](#departments-page)

- [Testing User Stories from User Experience (UX)](#testing-user-stories-from-user-experience--ux-)
  * [First Time User Goals](#first-time-user-goals-1)
  * [Returning User Goals](#returning-user-goals-1)
  * [Frequent User Goals](#frequent-user-goals-1)
  * [Admin User Goals](#admin-user-goals-1)

- [Further Testing](#further-testing)
  * [Brute-Forcing Attacks](#brute-forcing-attacks)
  * [404 Error Handling](#404-error-handling)
  * [Login Page](#login-page)
  * [Register Page](#register-page)
  * [Logout](#logout)

- [Deployment](#deployment)
  * [Repository](#repository)
    + [Forking the GitHub Repository](#forking-the-github-repository)
    + [Making a Local Clone](#making-a-local-clone)
    + [Terminal](#terminal)
    + [Further steps required](#further-steps-required)

  * [Deploy to Heroku](#deploy-to-heroku)

- [Credits](#credits)


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User Experience (UX)

The business goals are to establish the app as a reputable and reliable tool
that facilitates film production. It provides a communication platform for all 
areas of film production allowing messages, ideas and images to be sent
through each department channel. A future goal would be the development of 
of collaboratative areas for storyboarding, shotlist imaging pre-visualization.

For the user the goal of the app is to enhance and facilitate film production.
It will allow a simple and enjoyable means on departmental and inter-departmental
communication. It is streamlined for the exchange of messages by specific areas.
It will allow the user the means to instantaniously both share and recieve
ideas and all work related developements as they happen.

### Strategy Plane

The aim of the site is to create an app that facilitates film production and is on a par with the latest trends in digital communication media. It aims to be enjoyable and simple to use and become a “go to” tool in film production.
The site is designed to give the user, here being specifically the film production team, the necessary tools to communicate their ideas during production collaboration.  
Clearly separating the production process by department is key to the site’s simplicity and reliability of use where the user can fulfill their needs to find and post communications and images.
The owners of the site, here being the production team, have overall control over the site and the necessary tools, unique only to those given admin access, to update the script and the shot list and add and delete image in the image bank.
Security is a big factor in the site and only those give a key can register, the password functionality is secured through Werkzeug and the admin access id check both in the front and backend.

### Scope Plane

The features included in the app at present reflect choices made around what is absolutely necessary for the app to deliver it’s basic marketed functionality, which proposed features are buildable and what features are necessary to make
the app sellable. The buildable aspect was vital for the scope of the app and several more advance features, like a communal workspace and storyboarding facilities were repositioned as future features.

[Back to Table of Content](#table-of-content)

### Structure Plane

The site is structured so the user can navigate in an intuitive way through the different features, all pages keeping a uniformed consistency. 
The user is taken on a journey into the site, all elements being discoverable as they proceed along.
The User Base is central to the scructure. Here the user has a number of immediate
option tools they can click on. Or, as they are being visably encouraged to do so and
is the primary aspect to the app they can select a department. Once taken there
they are given different "find messages" choices they can follow.
They will see clear states of change when they interact with the features and be given clear feedback to assure them of their interactive success.
The information architecture is a tree structure allowing users to move through content quickly and simply becoming aware of the site’s inherent structure as they go. 

<h2 align="center">
<img src="documentation/readme-images/struc.png" width="90%">
</h2>

### Skeleton Plane

The interface is aesthetically functionally all the time creating a positive reaction in the user with every click, 
making the user feel both at home here and part of an exciting journey. Details of
this are found in the Design section.

[Back to Table of Content](#table-of-content)


### User stories

 - #### First Time User Goals

1. As a First Time User, I want to learn what the site has to offer and how to use the site quickly.
2. As a First Time User, I want to find communications in my or other departments.
3. As a First Time User, I want to view images.

  - #### Returning User Goals

4. As a Returning User, I want to download the latest shotlist and script
5. As a Returning User, I want to add a communication in a specific area.

  - #### Frequent User Goals

6. As a Frequent User, I want to view the latest production updates.
7. As a Frequent User, I want to edit and delete my communications.

8. As a Frequent User, I want to view and post communications and see images relating to style, 
   shooting and script choices so I can develop my owm choices accordingly.

  - #### Admin User Goals

1. As the admin user I want to upload the latest draft of the script.
2. As the admin user I want to upload the latest shotlist.
3. As the admin user I want to upload new images.
4. As the admin user I want to edit images.
5. As the admin user I want to delete images.
6. As the admin user I want to delete a user.
7. As the admin user I want control over material posted on the site for legal
   and other purposes.

[Back to Table of Content](#table-of-content)

## Design

<h2 align="center">
<img src="documentation/readme-images/log1.png" width="90%">
</h2>

### Colour Scheme
 - The site aims to be minimal streamlined and slick using an offblack background 
   colour with blue side image panels and an offwhite text. Crimson and blue tones
   are used minimally against this for a touch of sophisticated flare especially
   the site title in crimson letters running downwards on either side of the header box.

  
### Typography
 - Materialize was used for the site and I kept their inherent font-family style 
   choice with was: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, 
   Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif. This worked perfectly
   for the style of the site.


### Imagery
 - The site was designed to have a minimal straight to business slick slightly cinematic look. This was achieved
   by the use of right and reversed left narrow side panels on an offblack background.
   The panels contain an images of a narrow window and it's blue lighting
   effect which act as a foreground to the complementing seemingly distant dark header box
   container which also has one of the images to which focus is drawn. The hope is that
   this achieves a feeling of cinematic lighting and depth.

### Wireframes

 - PDF – Balsamic was used to design the layout for login, register, user base, 
   department messages, images, and the add and admin pages.

   [View on Github](https://github.com/johnston9/MS3-Shot-Caller)

[Back to Table of Content](#table-of-content)

## Existing Features

### Responsive Design

  The site is responsive to all sizes and the images remain whole and in proportion at all sizes.

<p align="center"> Large Screen 1600px</p>

<h2 align="center">
<img src="documentation/readme-images/post-16.png" width="90%">
</h2>

<p align="center">  Medium Screen 1000px</p>
<h2 align="center">
<img src="documentation/readme-images/post-md.png" width="90%">
</h2>


<p align="center"> Small Screen 370px</p>
<h2 align="center">
<img src="documentation/readme-images/post-sm.png" width="25%">
</h2>

[Back to Table of Content](#table-of-content)

### Login/Register Pages and Security Measures

  The user is brought first to the login page. From there they will find a 
  link to register if a new user. One of the core features of the site is it's
  built-in security measures.

  The first of which is the need for a register key to register. This will allow
  the owner of the site control over who is able to register. It would then be up to 
  them to give the necessary instructions to the user toensure that the key is not 
  further passed on. 

  As a minor security feature the login and register pages are not connected to the base
  page and the other pages.

  Werkzeug's security utilities "generate_password_hash" and "check_password_hash"
  are used run the register and login functions and ensure login security.
 
  Other security measures include front-end measures to allow admin access only to admin.
  This is backed up in the back-end ensuring only these admin functions will run if
  admin is the sesson user.

  All other functions in the back-end are protected by ensuring that there is a sesson
  user for them to run, and only registered users would be logged in and set as sesson users.


<p align="center">Register Page</p>
<h2 align="center">
<img src="documentation/readme-images/reg1.png" width="90%">
</h2>

 See Further Testing login and register pages.

 - [Back to Table of Content](#table-of-content)

### User Base Page

  Once loged in the user is taken to their own User Base page which is the center base
  of the site and along with all other pages had a navbar to take them to any page.
  They will immediatly see a "Latest Updates" button which they can click on to take
  then directly to a page showing that dayy's production messages. This in intended a a primary
  feature in the app that allows all crew members to stay on top of all of current developments.

<p align="center">Latest Updates</p>
<h2 align="center">
<img src="documentation/readme-images/la.png" width="90%">
</h2>


  The bulk of the page is used to show the different departments on which the user can
  click to view each department's communications. 
  The core feature of the site is clarity and specificy. The first measure of this is the 
  seperating of the production communications into different departments.

  This page also allows the user to download the latest script and shotlist, to add messages 
  and provides a link to take them to the images page.

<p align="center">User Base Department Choices</p>
<h2 align="center">
<img src="documentation/readme-images/depts1.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

### Departments Page

  Once the user clicks on a department they are taken to that department 
  Find by Date Page. That day's communications will automatically be displaying.
  All messages open on click to reveal the contained message and images contained in
  it if there were any posted.
  
<p align="center">Today's communications</p>
<h2 align="center">
<img src="documentation/readme-images/dep-1.png" width="90%">
</h2>
 
  The user has the further options of finding all communications in that
  department.
  
<p align="center">All communications</p>
<h2 align="center">
<img src="documentation/readme-images/dep-2.png" width="90%">
</h2>

  Also the user can find them by specific date by using the Datepicker.

<p align="center">Pick Date (on small screen</p>
<h2 align="center">
<img src="documentation/readme-images/cam23.png" width="25%">
</h2>

<p align="center">Result of Pick Date (on large screen</p>
<h2 align="center">
<img src="documentation/readme-images/cam22.png" width="50%">
</h2>

  The user can also click on a link to take them to the Find by Poster Page where they
  can find communications by entering the poster's name. 

<p align="center">Find by Poster Page with message open and containing an image</p>
<h2 align="center">
<img src="documentation/readme-images/dep1.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

### Images Page
    
  The user here can find images by entering a specific image tag name if they have 
  it or entering a search word relating to the images they wish to see. These image
  are only upload by admin so they are intended to be actual style and shooting choices,
  options of these. Here the admin can set images for users to know what choices
  have been made and what looks and themes are being uses.  
  In the Departments posting message option it also allows for the posting of images
  for discussion and collaboration.

<p align="center">Images Page</p>
<h2 align="center">
<img src="documentation/readme-images/hos1.png" width="90%">
</h2>

 If no image is found for a query a message is displayed.

<h2 align="center">
<img src="documentation/readme-images/no-im.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

### Admin Page

  As discussed above in "Security Measures" defensive programming will only allow
  access to the admin features if admin is the sesson user and this is inplemented
  both in the front-end and back-end. If the user is admin they will be given the 
  option to delete a user, upload the latest script, upload the latest shotlist 
  or upload new images.

<p align="center">Admin Page 1600px</p>
<h2 align="center">
<img src="documentation/readme-images/admin1.png" width="90%">
</h2>

<p align="center">Admin Page 375px</p>

<h2 align="center">
<img src="documentation/readme-images/admin2.png" width="25%">
</h2>

Please see admin testing for further details.

[Back to Table of Content](#table-of-content)

## Database structure

MongoDB was used as the site's database and held 14 collections. 

1 - <strong>latest_script</strong> - to hold the script url.

2 - <strong>shotlist</strong> - to hold the shotlist url.

3 - <strong>users</strong> - to hold the user's details.

4 - <strong>images</strong> - to hold the image bank images ref names, descriptions and urls.

5 - <strong>depts</strong> - to hold the departments names, titles and the department images urls for User Base/Department's pages.

6-14 - <strong>9 collections</strong> for each of the departments messages.

There is an Entity Relationship between the users collection and the 9 seperate departments
collections on "username" and "job_title". A third relationship
is between the concatenated result of the users collection "firstname" and "lastname"
values and the department collection's "poster". These allow the automatic input 
of these user valies when a user sends a message.

There is an Entity Relationship between depts and the 9 departments on depts dep_name and
the actual name of the department collection. This allow for the
depts dep_name to be passed to app.py when a department is clicked on in the user's
base page. This sends dep_name as a variable to the get_dep function in app.py allowing
it to be used in the find() method on Mongo and get the messages for the collection of that name.

<strong>Note 1:</strong> In the ER Diagram the last relationship above points to the the dep_name in the example camera
      collection as it was not technically posssible to have it point to the collection name, which
      is in fact the correct relationship.

<strong>Note 2:</strong>: Only one, "camera", of the 9 department collections is used in the diagram but the same
      relationships exist for all of the 9 department collections.

<strong>Note 3:</strong> Two values in the images collection, image_name and image_src, share the same names as ones
      in the department collection but this is not actually used by any python function. If admin 
      wants to use one of the message images they would do so manually on the spot by right clicking on it.
      Also they may wish to alter the image_name for various reasons.

<h2 align="center">
<img src="documentation/readme-images/er.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

The MongoDB Shot Caller database contains the following collections.

<p align="center"> <strong>users</strong>- for user details</p>

<h2 align="center">
<img src="documentation/readme-images/m-users.png" width="90%">
</h2>


<p align="center"><strong>depts</strong>- for each department's details</p>

<h2 align="center">
<img src="documentation/readme-images/m-departments.png" width="90%">
</h2>


<p align="center"><strong>9 department collections, e.g. camera</strong> - each containing that department's messages</p>

<h2 align="center">
<img src="documentation/readme-images/m-dep1.png" width="90%">
</h2>


<p align="center"><strong>images</strong> - for image details</p>

<h2 align="center">
<img src="documentation/readme-images/m-images.png" width="90%">
</h2>


<p align="center"><strong>shotlist</strong> - for the shotlist's url</p>

<h2 align="center">
<img src="documentation/readme-images/m-shotlist.png" width="90%">
</h2>


<p align="center"><strong>script</strong> - for the script's url</p>

<h2 align="center">
<img src="documentation/readme-images/m-script.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)


## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)
- [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
- [JINJA](https://en.wikipedia.org/wiki/Jinja_(template_engine))

## Frameworks, Databases, Libraries & Programs Used

1. [Materialize:](https://materializecss.com/getting-started.html)
   - Materialize was used to create the overall framework and it's grid based 
     format for the site and it's primary responsiveness. Also specific 
     Materialize features were used throughout which include the, collapsable, 
     the navbar and sidenav, the modals, the tooltipped feature, the datepickers
     and the overall styling of the website.
1. [Flask:](https://en.wikipedia.org/wiki/Flask_(web_framework))
   - Flask was used along with python to build then site's backend framework and
     run the app.
1. [Werkzeug:](https://werkzeug.palletsprojects.com/en/1.0.x/)
   - Flask used Werkzeug to the application to speak with the webserver and 
     for security purposes mainly with regard to the users's password.
1. [Jinja:](https://en.wikipedia.org/wiki/Jinja_(template_engine))
   - Flask used the Jinja template engine to build the front-end of the app.
1. [MongoDB:](https://en.wikipedia.org/wiki/MongoDB)
   - MongoDB was used as the app's backend database.
1. [Pymongo:](https://pypi.org/project/pymongo/)
   - Pymongo was used for interacting with MongoDB database from the app.
1. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used throughout the website for the arrow navigation and
     a number of other icons.
1. [jQuery:](https://jquery.com/)
   - jQuery was used along with javascript to initialize the Materialize features.
1. [Git](https://git-scm.com/)
   - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](https://github.com/johnston9/MS3-Shot-Caller) during the design process.
1. [Freeformatter](https://www.freeformatter.com/html-formatter.html)
   - Freeformatter was used to tidy up the final code.
1. [Gauger](https://gauger.io/fonticon/)
   - Gauger was used to create the favicon icon.
1. [Am-I-Responsive](http://ami.responsivedesign.is/):
   - Am I Responsive was used to test the site's responsive sizings and to generate responsive sizing images.
1. [GitHub Wiki TOC generator:](http://ecotrust-canada.github.io/markdown-toc/)
   - GitHub Wiki TOC generator was used to create the Table of Contents.
1. [dbdiagram.io](https://dbdiagram.io/home)
   - dbdiagram.io was used to create the Entity-Relationship Diagram.

[Back to Table of Content](#table-of-content)

## Testing

W3C Markup Validator, W3C CSS Validator. PEP8 and JSHint were used to validate every page of the project.

- [W3C Markup Validator](https://validator.w3.org/) - [Results](https://github.com/johnston9/MS3-Shot-Caller)
  - W3C "Direct Input" option was used on each html page. As Jinja was used throughout the site
    errors displayed where it was used on each page but no other error displayed, documentation -folder "w3c-direct-input".
    When I validated by URL no errors were shown as seen in documentation "w3c-by-url".

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/johnston9/MS3-Shot-Caller)
  - W3C showed no errors and only one warning for the hr rule's background colour
    being the same as it's colour, which was intentional.
  
- [JSHint](https://jshint.com/) - [Results](https://github.com/johnston9/ms2-apis)
  - JSHint was used with "New JavaScript features (ES6)" and "jQuery" checked in the configuration menu.
    All files were clear of errors and warnings.
    
- [PEP8 online check](http://pep8online.com/) - [Results](https://github.com/johnston9/MS3-Shot-Caller)
  - PEP8 approved the app.py page and all python apart from saying "no newline at end of file"
    but I researched this and found it was a common result and could be ignored.

[Back to Table of Content](#table-of-content)

## Lighthouse

Lighthouse was used to test every page in desktop and moblie screens.

### Sumary of Issues 

1. On all pages apart from the Login and Register "Not Secure" displayed in the address 
   and Best Practices had a "Does not use HTTPS - insecure requests found" error. 
   This is because I was using basic Heroku and can fix this if I purchace an SSL certificate.

<p align="center"><strong>Does not use https message</strong></p>
<h2 align="center">
<img src="documentation/readme-images/not-sec.png" width="90%">
</h2>

2. Lighthouse gave me an accessibility note for the header "Shot Caller" decorative
   writing in red either side of the header box. As this is purely decorative and is only barely visual limited I left it
   red as this was in keeping with my style intentions. I did however change it from Crimson
   to a bright red. See User Base page - Accessibility below for more on that issue.

3. On the User Base and Departments pages Lighthouse gave me a Best Practices messages 
   regarding the image sizes. See User Base page below for more on that issue.

4. Lighthouse gave me an accessibility note for the select dropdown trigger on the Add Message page
   not having a label but it does have one for the outer select so this is a Materialize issue.
   See Add Message page below for more on that issue.

### Sumary of Issues resolved

1. On first report Lighthouse gave me an accessibility note for the sidenav icon not having a name or label.
   I added 'aria-label="Menu"' and the issue was resolved.

2. On first report Lighthouse gave me an insecure link warning for the link to Cloudinary 
   I put rel="noopener" in all links and the issue was resolved.


### Login page

On first report Lighthouse gave me an accessibility note for the submit button and 
register link but I changed the colours and the issue was resolved. Desktop and mobile
results the same.

<p align="center"><strong>Desktop</strong></p>
<h2 align="center">
<img src="documentation/readme-images/log2.png" width="90%">
</h2>


### Register page

As above same result for desktop and mobile. 

<p align="center"><strong>Desktop</strong></p>
<h2 align="center">
<img src="documentation/readme-images/reg2.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

### User Base page 

 - #### Best Practices

On first report Lighthouse gave me a Best Ptactices note for images not being sized with the correct aspect ratio. I resized
the images to the desire 2:3 ratio. Below is an image detailing the Best Practices
with only the HTTPS error common to all pages.


<p align="center"><strong> User Base page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/user1a.png" width="90%">
</h2>

 - Mobile

I also resized the images to the desired 50px by 50px for mobile devices but the only way I could
use them with the Jinja Template was to create two img elements in the for loop code block
and set one to display "none" at larger than 600px in CSSand the opposite for the other. I decided against doing this weighing 
the slight improvment in Best Practices and the improvment in Performance against cleaner, shorter code
minimizing any risk no matter how small.
That said should the app the taken to a further stage I will investsigate it more.

<p align="center"><strong> Mobile result</strong></p>
<h2 align="center">
<img src="documentation/readme-images/user2b.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

 - #### Accessibility

Lighthouse gave me an accessibility note for the header "Shot Caller" decorative
writing in red either side of the header box. As this is purely decorative and is only barely visual limited I left it
red as this was in keeping with my style intentions. I did however change it from Crimson
to a bright red.

This report was for every page on the site and accounted solely for the "97" score that
was given for "Accessibility" on this and all other pages apart from Add Message. I will include 
the image here that would be similar for all pages.

<p align="center"><strong>Header red text note</strong></p>
<h2 align="center">
<img src="documentation/readme-images/assp.png" width="90%">
</h2>


 - The extra buttons on the admin user page did not effect the results.

 [Back to Table of Content](#table-of-content)


 - ### Edit Message page

<p align="center"><strong>Desktop</strong></p>
<h2 align="center">
<img src="documentation/readme-images/.png" width="90%">
</h2>

 - ### Add Message page

<p align="center"><strong>Desktop</strong></p>
<h2 align="center">
<img src="documentation/readme-images/messy.png" width="90%">
</h2>


[Back to Table of Content](#table-of-content)

 - ### Departments page

   The Departments page had the same results as the User Base page.

<p align="center"><strong>Desktop</strong></p>
<h2 align="center">
<img src="documentation/readme-images/d-lar.png" width="90%">
</h2>

<p align="center"><strong>Mobile</strong></p>
<h2 align="center">
<img src="documentation/readme-images/depts-mo.png" width="90%">
</h2>

 - ### Latest Production Updates page

<p align="center"><strong>Desktop</strong></p>
<h2 align="center">
<img src="documentation/readme-images/late.png" width="90%">
</h2>

 - ### Admin pages - 

   All 4 pages had the same results.

<p align="center"><strong>Remove User page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/admin-remo.png" width="90%">
</h2>

<p align="center"><strong>Add Latest Script page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/ad-a.png" width="90%">
</h2>

### Lighthouse internal strange occurance

1. Lighthouse gave me an error for the robot.txt not being valid one time
   but never again.  
    
<p align="center"><strong>Robot.txt warning</strong></p>
<h2 align="center">
<img src="documentation/readme-images/robo.png" width="90%">
</h2>


[Back to Table of Content](#table-of-content)


## Testing User Stories from User Experience (UX) 

### First Time User Goals

1. #### As a First Time User, I want to learn what the site has to offer and how to use the site quickly.

    1. The site is designed for first time learning. It is streamlined for specicic
       user goals that after first use are so simple that with a few clicks after entering
       the site the user will be able to get to any specific area or tool. At the top of the 
       User Base Page and throughout the site the navbar displays all options for the user
       so they can select their desired destination quickly.
    2. Upon entering the user is taken to their home base and greeted with image
       links for each production department and the message to "Choose Department".
       Upon clicking on a department they are taken to that departments "Find by Date Page"
       where that day's communications are automatically showing.
       They are given further choices to find all messages or go to the "Find by Poster Page".
       The user will become automatically aware of what is on offer and how to find a particular
       field in a few click. The user will see the choices on offer and learn how best 
       to use them for their needs.
    3. Below the departments on the User Base Page the user will see further options
       to add messages, search images, download the script or download the shotlist.

<p align="center"><strong>User Base</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/user10.png" width="90%">
</h2>


2. #### As a First Time User, I want to find communications in my or other departments.

    1. Upon opening a department page the user will see the latest messages displayed.
       They will see the option to open all messages and a more specicic option
       to find messages by a particular date.
    2. The user will see a further option to go to "Find messages by Poster" and on clicking
       they will be taken to the "Find messages by Poster Page" where they can get all messages
       from a particular team member by typing in their full name as instructed.
    3. The user will see all chosen messages each displaying,in the header the name and position
       of the poster, the subject and whether it is a priority or not. On clicking on a message box
       it will open to show the message and an image if one has been posted.
    4. If there are no messages for a particular request a message will display
       advising the user of this.

<p align="center"><strong>Departments</strong></p>
<h2 align="center">
<img src="documentation/readme-images/dep-post.png" width="90%">
</h2>

<p align="center"><strong>No Dessages Display</strong></p>
<h2 align="center">
<img src="documentation/readme-images/no-mes.png" width="90%">
</h2>

3. #### As a First Time User, I want to view images.

    1. In the navbar and on their home base the user will see a link to search images
       which on clicking will take them to the images page.
    2. The user will see instruction on how to search for images. They can use a specicic
       image reference tag, if thet have one or they can input search words relevent
       to what they are looking for.
    3. The image bank is uploaded by the production team only so only contains sanctioned
       images of style choices, locations and other images all in keeping with the choices
       set by the team or different options that are being worked on or considered.

<p align="center"><strong>Specific reference tag input</strong></p>
<h2 align="center">
<img src="documentation/readme-images/im-spec.png" width="90%">
</h2>

<p align="center"><strong>Specific reference tag result</strong></strong></p>
<h2 align="center">
<img src="documentation/readme-images/im-res1.png" width="90%">
</h2>

<p align="center"><strong>Result for query word "nick"</strong></p>
<h2 align="center">
<img src="documentation/readme-images/nick-all1.png" width="25%">
</h2>

[Back to Table of Content](#table-of-content)

### Returning User Goals

4. #### As a Returning User, I want to download the latest shotlist and script.

    1. On clicking download script the script is downloaded to the user's device.

    1. On clicking download shotlist the shotlist is downloaded to the user's device.

<p align="center"><strong>Result for downloaded shotlist</strong></p>
<h2 align="center">
<img src="documentation/readme-images/shot1.png" width="90%">
</h2>

<p align="center"><strong>Result for downloaded script</strong></p>
<h2 align="center">
<img src="documentation/readme-images/script1.png" width="90%">
</h2>


5. #### As a Returning User, I want to add a communication in a specific area.

    1. In the navbar, on the User's Base page and in all the department
       pages the user will see a button to "Add Message". 
    2. On clicking the button the user is brought to the "Add Messsage" page
       where they can post a new communication. A flash message will displayed
       if their message has been added successfully.
    3. They are also given the option to add an image and instructions on how to do 
       so are supplied. 


<p align="center"><strong>Add message page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/add-11.png" width="25%">
</h2>

<p align="center"><strong>Success Flash message</strong></p>
<h2 align="center">
<img src="documentation/readme-images/add-13.png" width="90%">
</h2>

<p align="center"><strong>Result</strong></p>
<h2 align="center">
<img src="documentation/readme-images/add-12.png" width="90%">
</h2>


[Back to Table of Content](#table-of-content)


### Frequent User Goals

6. #### As a Frequent User, I want to view the latest production updates.

   1. When the user clicks on the Latest Updates buttton on their home base page they are taken to the Today's
      Latest Production Updates Page. All the production communications from that day are
      shown there.
      There is also a link to take them straight to all other departments to see their latest
      updates which are always displaying for that day.

  
<p align="center"><strong>Latest Updates Page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/la2.png" width="90%">
</h2>

7. #### As a Frequent User, I want to edit and delete my communications.

    1. The user and strictly only the user, not even the admin, will have
       edit and delete buttons display under the messages that they themselves have
       posted. 
    2. With a click they will be taken to the "Edit Message" page where they can edit their message.
       They will get a flash message to tell them if the edit was a success.

<p align="center"><strong>Message before edit</strong></p>
<h2 align="center">
<img src="documentation/readme-images/ed-b.png" width="90%">
</h2>

<p align="center"><strong>Edit page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/edit.png" width="90%">
</h2>

<p align="center"><strong>Message after edit</strong></p>
<h2 align="center">
<img src="documentation/readme-images/ed-a.png" width="90%">
</h2>

<p align="center"><strong>Flash message</strong></p>
<h2 align="center">
<img src="documentation/readme-images/edit-fl.png" width="90%">
</h2>

3. On clicking delete will be given a modal warning asking if they are sure
       they want to delete the message and a flash message telling them if the 
       delete was a success should they click OK.

<p align="center"><strong>Delete Modal</strong></p>
<h2 align="center">
<img src="documentation/readme-images/del-m.png" width="90%">
</h2>

<p align="center"><strong>Flash Message</strong></p>
<h2 align="center">
<img src="documentation/readme-images/del-f.png" width="90%">
</h2>

8. #### As a Frequent User, I want to view and post communications and images relating to my style, 
   shooting and script choices.

   1. Having used the app once the user will be easily able to navigate
       through it to locate desired fields of messages by date, department and poster. 
   2. Having used the app once the user will be easily find how to post all communications
       and images.
   3. Having used the app once the user will be easily able to download the script
       and shotlist. 

### Admin User Goals


1. #### As the admin user I want to upload the latest draft of the script.

   - If the admin user clicks the upload script button available only to them they
     will be taken to the "Add Latest Script" page. They can follow the instructions
     telling them how to upload and get an SRC for the new file from Cloudinary, 
     or a similar app, and enter an SRC here.
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

- They will get a flash message to tell them if it was sucessful. 

<h2 align="center">
<img src="documentation/readme-images/sc-2.png" width="90%">
</h2>

2. #### As the admin user I want to upload the latest shotlist.

   - If the admin user clicks the upload shotlist button available only to them they
     will be taken to the "Add Latest shotlist" page. They can follow the instructions
     telling them how to upload and get an SRC for the new file from Cloudinary, 
     or a similar app, and enter an SRC here.
     
<h2 align="center">
<img src="documentation/readme-images/st-1.png" width="90%">
</h2>

- They will get a flash message to tell them if it was sucessful. 

<h2 align="center">
<img src="documentation/readme-images/st-2.png" width="90%">
</h2>

3. #### As the admin user I want to upload new images.

   - If the admin user clicks the upload images button available only to them they
     will be taken to the "Add New Images" page. They can follow the instructions
     telling them how to upload and get an SRC for the new file from Cloudinary, 
     or a similar app, and enter an SRC here. They will also be told that if they
     want to use an image already uploades by a user in the department messages they
     can just right click on the image and enter it here.
     
<h2 align="center">
<img src="documentation/readme-images/st-1.png" width="90%">
</h2>

- They will get a flash message to tell them if it was sucessful.

<h2 align="center">
<img src="documentation/readme-images/st-2.png" width="90%">
</h2>

4. #### As the admin user I want to edit images.

   - On the images page under every image an edit button will display for
     the admin and the admin only. 

<h2 align="center">
<img src="documentation/readme-images/ee-1.png" width="90%">
</h2>
          
   - On clicking it they will be taken to the
     "Edit Image" page where they can update any of the three image values.
     
<h2 align="center">
<img src="documentation/readme-images/ee-2.png" width="90%">
</h2>

- They will get a flash message to tell them if it was sucessful.

<h2 align="center">
<img src="documentation/readme-images/ee-4.png" width="90%">
</h2>

5. #### As the admin user I want to delete images.

   - On the images page under every image a delete button will display for
     the admin and the admin only. On clicking they will be given a modal
     asking them to confirm. On doing so they will get a flash message.
     
<h2 align="center">
<img src="documentation/readme-images/delet.png" width="90%">
</h2>

- They will get a flash message to tell them if it was sucessful.

<h2 align="center">
<img src="documentation/readme-images/sc-2.png" width="90%">
</h2>

6. #### As the admin user I want to delete a user.

   - If the admin user clicks the "Remove User" button available only to them they
     will be taken to the "Remove User" page. They must enter the user's firstname they
     seperatly the user's lastname then press submit. They will get a flash message on
     completion. No modal use deemed necessary as this is an already involved process.
     
<h2 align="center">
<img src="documentation/readme-images/rm.png" width="90%">
</h2>

- They will get a flash message to tell them if it was sucessful.

<h2 align="center">
<img src="documentation/readme-images/st-2.png" width="90%">
</h2>

7. #### As the admin user I want control over material posted on the site for legal
   and other purposes.

   - Admin will have access to the edit and delete functions for every message
     along with the user who posted the message. This along with the remove user function
     will allow admin full control of the site;

<h2 align="center">
<img src="documentation/readme-images/ad-4.png" width="90%">
</h2>


## Further Testing


### Brute-Forcing Attacks

- If a user tries a brute-force entry using a known user's username with the Base Page URL
  they will get an Internal Server Error message.

<h2 align="center">
<img src="documentation/readme-images/brut-user.png" width="50%">
</h2>

- If a user tries a brute-force entry using a known view, e.g. get_depts, 
  or a view that takes an argument without the argument, e.g. get_dep,
  or a view that takes an argument with a correct argument, e.g. get_dep/camera
  they will get an Internal Server Error message.
  
<h2 align="center">
<img src="documentation/readme-images/brut-get.png" width="50%">
</h2>

- If a user tries a brute-force entry using any other characters after the address
  they will get an Internal Server Error message.
<h2 align="center">
<img src="documentation/readme-images/brut-xxx.png" width="50%">
</h2>

### 404 Error Handling

- If a user is logged in as a sesson user and they get a 404 error they will be directed to a custom page
  with a link back to their home base page. This page was build without 
  a favicone link or any the other pages' metadata in the head intentionally.

<h2 align="center">
<img src="documentation/readme-images/page-n.png" width="50%">
</h2>

- When they click on the link on the page they are brought back to their home base.

<h2 align="center">
<img src="documentation/readme-images/back.png" width="50%">
</h2>

### 500 Error Handling

- If a user is logged in as a sesson user and they get a 500 error they will be directed to a custom page
  with a link back to their home base page. This page was build without 
  a favicone link or any the other pages' metadata in the head intentionally.


### Login Page
 
 - If user's "Username" entry does not match the requested format they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/logu.png" width="50%">
</h2>

 - If user's "Password" entry does not match the requested format they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/log-p.png" width="50%">
</h2>


- If user's "Username" or "Password" do not match to ones stored on the database 
   they get a flash "Incorrect Entry" message.

<h2 align="center">
<img src="documentation/readme-images/log-x.png" width="50%">s
</h2>

### Register Page
 
 - If user's "Username" entry does not match the requested min length format they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/reg1.png" width="50%">
</h2>

 - If user's "Username" entry does not match the requested character format they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/reg1a.png" width="50%">
</h2>

 - If user does not fill in the required "First Name" field they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/regf.png" width="50%">
</h2>

 - If user does not fill in the required "Last Name" field they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/regl.png" width="50%">
</h2>

 - If user does not fill in the required "Job Title" field they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/regj.png" width="50%">
</h2>

 - If user's "Password" entry does not match the requested character or length format they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/regp.png" width="50%">
</h2>

 - If user does not enter a key they get a warning message.

<h2 align="center">
<img src="documentation/readme-images/regk.png" width="50%">
</h2>

 - If user enters an incorrect key they get a flash "Invalid Key" message.

<h2 align="center">
<img src="documentation/readme-images/regk2.png" width="50%">
</h2>


- The app was tested on Google Chrome, Internet Explorer, and Safari browsers.

- The app was viewed on a variety of devices such as Desktop, Laptop, iPhone and various other smartphones.

- Friends and family members were asked to review the site and to point out any bugs and/or user experience issues. These were taken on board and changes were made if necessary or to give a better user experience.

[Back to Table of Content](#table-of-content)

### Logout

The logout button remove the user from sesson user and displays a Flash message if this is
sucessful.

<h2 align="center">
<img src="documentation/readme-images/logout.png" width="50%">
</h2>

### Known Bugs

- All bugs to date have been dealt with. The only issue is that on my laptop the select department
  input box red line warning on the add message page remain red after a department is selected.
  On all other devices including a number of turors, who I check the issue with it works
  , i.e. it turns green. Example below from a smart phone of it working correctly.

<h2 align="center">
<img src="documentation/readme-images/select.png" width="25%">
</h2>

### A Code Note

For the add_script function I got the object_id for the original document to be updated
by having Flask get the Mongo latest_script collection, passing that to the Jinja template
so it could get the id and pass that back to the Flask as an argument.

For the add_shotlist function I just set the object_id for the document directly in
the function.

The reason for this is just to have options for further development of the app as to which
method wold be most appropriate.


[Back to Table of Content](#table-of-content)

## Deployment

### Development platform

1. [Gitpod:](https://www.gitpod.io/docs/)
   - Gitpod was used as the development platform.

### Repository
   [Github](https://github.com/)
   - Github was used as the repository for the project.

#### Forking the GitHub Repository

By forking we make a copy of the GitHub Repository in our Github account.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/johnston9/MS3-Shot-Caller)
2. At the top of the Repository just above the "Settings" button on the menu, click the "Fork" Button.
3. This will create a copy of the original repository in your GitHub account.

#### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/johnston9/MS3-Shot-Caller)
2. Under the repository name, click "Code" beside the Gitpod bitton.
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash.
5. Set the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL copied above.
7. Press enter and a local clone will be created.
8. You may want to unpack the everything from the containing "MS3-Shot-Caller" folder.
9. The clone will include two file needed for set up and Heroku.

  1. The requirements.txt which contains all packages to be installed to run the app. These are  
  Flask-PyMongo, dnspython and Flask and it's dependencies. Heroku
  will need these to run the app.

  2. The Procfile which tells Heroku what language the app is using.

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.


#### Terminal

  - Use the following command to install the packages needed for the app from 
    requirements.txt. 

##### pip3 install -r requirements.txt 
  - The -r switch tells pip to install packages from the requirements.txt file 
    needed for the app.

#### Further steps required  

Some files containing sensitive variables will not have been pushed to Github so it 
will be necessary to create them.

##### Create a .gitignore file
- .gitignore is used to store sensitive variables and keys that do not get sent to github.
  Type pycach.py and env.py in the .gitignore file.

##### Create a env.py file 
- In env.py set the app's environment variables and keys needed during development.
  These will later be set in Heroku.


    **env.py**

      import os

      os.environ.setdefault("IP", "0.0.0.0")

      os.environ.setdefault("PORT", "5000")

      os.environ.setdefault("SECRET_KEY", "***************")

      os.environ.setdefault("REGISTER_KEY", "************")

      os.environ.setdefault("MONGO_URI", "Get this in Mongo when you click 
      'Connect your Application’ after clicking the Connect button")
      
      os.environ.setdefault("MONGO_DBNAME", "The name of your Mongo database") 


### Deploy to Heroku

[Heroku](https://www.heroku.com/platform)

#### Heroku was used to deploy the project.

 - As mentioned in the "Clone" section above a requirements.txt and Procfile are needed
by Heroku to run the app. If not already created make sure to do so. In the terminal
type they following commands.

   - pip3 freeze --local > requirements.txt
   - echo web: python3 app.py > Procfile

 - Register a Heroku account.

 - Click 'Create a New App'.

 - Where asked select "Europe" as the region then click create app.

 - Click Settings then click Reveal Config Vars.

 - Now set the variables and keys to those in env.py.

     - IP, with the value of 0.0.0.0.

     - PORT, which is 5000.

     - SECRET_KEY, copy then paste it from env.py. 

     - REGISTER_KEY, ************

     - MONGO_URI, get this when 'Connect your Application’ is clicked on in Mongo connect area.

     - MONGO_DBNAME, The name of your Mongo database.

- THEN CLICK HIDE CONFIG VARS

 - Back in Deploy choose Github then click Search to get the correct Github repo for the app
   then click connect.

 - Click Enable Automatic Deployment then click Deploy Branch.

 - Click "View" to launch the app.

#### Clarification

Clarification on steps taken in the terminal to create the app using pip3 
to install packages without requirements.txt and how to create the Procfile. 

##### pip3 install Flask

##### pip3 install flask-pymongo
- So Flask can communicate with Mongo install 'flask-pymongo'.

##### pip3 install dnspython
- Install 'dnsython' in order to use the Mongo SRV connection string.

##### echo web: python app.py > Procfile
- This tells Heroku what language the app is using.

##### 6. pip3 freeze --local > requirements.txt
- A requirements.txt containing all Flask dependencies is needed for Heroku to run the app.

[Back to Table of Content](#table-of-content)


## Credits

### Code

- [W3schools.com](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp): 
  Here I learnt how to create the return to top function.
- The general structure of the app was inspired by Tim Nelson's Task Manager app
  which is part of the Code Institute's course.
- The code to fix Materialize bug to show red line warning if department not 
  selected in add message is taken from Tim Nelson's Task Manager app.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/): 
  Here I got the code for the 404 custome error message.

### Content

All content was written by the developer.

### Media

The photos used in the image bank and used for messages Sthis site were obtained from;

  1.  [FreeImages.com](https://www.freeimages.com/)

  2.  [pexels.com](https://www.pexels.com)


The nine images used for the departments in this site were all created by myself 
using a small portion of different screenshots I took from the TV series "Arrow" 
created by "The CW Network", USA and the TV series "Gotham" created by "The Fox Broadcasting Company", USA.

These are only being used for the MS3 project and will be replaced if the app is
to be made in any way public.

I researched the topic of copyright when it comes to the use of screenshots of tv shows
used for non-profit purposes and concluded that the use of fragments of these images 
in this manner in the app come under the "Fair Use Doctrine". Also in terms
of the 4-factor balancing test that it is accessed under the usage in this project is fair.
I also cleared it with the college staff.


### Acknowledgements
   
- I'd like to thank the Code Institute tutor team for their support and  
Aaron Sinnott for his insights.

[Back to Table of Content](#table-of-content)













