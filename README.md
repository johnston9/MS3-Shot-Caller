<h1 align="center">Shot Caller - Movie Production Website</h1>

[View the project live here.](https://ms3-shot-caller.herokuapp.com/)

A web application for film production that provides a reliable all encompassing
means of production collaboration from pre-production to post. The app is designed 
to provide a simple streamlined means of communication through the different 
departments channels of film production. It allows both a general and specific 
means on searching and uploading communications and images to different departments.

It has a secure admin facility for site regulation and the upkeep of the image
bank that includes a simple means of uploading the latest script, shotlist.

Currently the app is limited to one production but future developements would
lead to it being turned into a piece of software that can be downloaded and used
as a product on an individual basis for each new production and owner.

<h2 align="center"><img src="documentation/readme-images/user16.png"></h2>

# Table of Content

- [User Experience (UX)](#user-experience--ux-)
  * [User stories](#user-stories)
    + [First Time User Goals](#first-time-user-goals)
    + [Returning User Goals](#returning-user-goals)
    + [Frequent User Goals](#frequent-user-goals)
- [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
- [Existing Features](#existing-features)
  * [Responsive Design](#responsive-design)
  * [Login/Register Pages and Security Measures](#login-register-pages-and-security-measures)
  * [User Base Page](#user-base-page)
  * [Departments Page](#departments-page)
  * [Images Page](#images-page)
  * [Admin Page](#admin-page) 
- [Languages Used](#languages-used)
- [Frameworks, Libraries & Programs Used](#frameworks--libraries---programs-used)
- [Testing](#testing)
  * [Credits](#credits)
  * [Code](#code)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# User Experience (UX)

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


## User stories

 - ### First Time User Goals

1. As a First Time User, I want to learn what the site has to offer and how to use the site quickly.
2. As a First Time User, I want to find and add communications in my department.
3. As a First Time User, I want to upload and view images.

  - ### Returning User Goals

4. As a Returning User, I want to download the latest shotlist and script
5. As a Returning User, I want to find messages in specific areas.
6. As a Returning User, I want to edit or delete my communications.

  - ### Frequent User Goals

7. As a Frequent User, I want to view communications and see images relating to style, 
   shooting and script choices so I can develop my owm choices accordingly.
8. As a Frequent User, I want to post communications and images relating to my style, 
   shooting and script choices.
9. As a Frequent User, I want to collaborate with other user on specific areas of 
   production.

[Back to Table of Content](#table-of-content)

# Design

<h2 align="center">
<img src="documentation/readme-images/log1.png" width="90%">
</h2>

## Colour Scheme
 - The site aims to be minimal streamlined and slick using an offblack background 
   colour with blue side image panels and an offwhite text. Crimson and blue tones
   are used minimally against this for a touch of sophisticated flare especially
   the site title in crimson letters running downwards on either side of the header box.

  
## Typography
 - Materialize was used for the site and I kept their inherent font-family style 
   choice with was: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, 
   Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif. This worked perfectly
   for the style of the site.


## Imagery
 - The site was designed to have a minimal straight to business slick slightly cinematic look. This was achieved
   by the use of right and reversed left narrow side panels on an offblack background.
   The panels contain an images of a narrow window and it's blue lighting
   effect which act as a foreground to the complementing seemingly distant dark header box
   container which also has one of the images to which focus is drawn. The hope is that
   this achieves a feeling of cinematic lighting and depth.

## Wireframes

 - PDF – Balsamic was used to design the layout for login, register, user base, 
   department messages, images, and the add and admin pages.

   [View on Github](https://github.com/johnston9/MS3-Shot-Caller)

[Back to Table of Content](#table-of-content)

# Existing Features

## Responsive Design

  The site is responsive to all sizes and the images remain whole and in proportion at all sizes.


<p align="center"> Large Screen 1600px</p>

<h2 align="center">
<img src="documentation/readme-images/post-16.png" width="50%">
</h2>

<p align="center">  Medium Screen 1000px</p>
<h2 align="center">
<img src="documentation/readme-images/post-md.png" width="50%">
</h2>


<p align="center"> Small Screen 370px</p>
<h2 align="center">
<img src="documentation/readme-images/post-sm.png" width="25%">
</h2>

[Back to Table of Content](#table-of-content)

## Login/Register Pages and Security Measures

  The user is brought first to the login page. From there they will find a 
  link to register if a new user. One of the core features of the site is it's
  built-in security measures.

  The first of which is the need for a register key to register. This will allow
  the owner of the site control over who is able to register. It would then be up to 
  them to give the necessary instructions to the user toensure that the key is not 
  further passed on. 

  As a minor security feature the login and register pages are not connected to the base
  page and the other pages.

  Other security measures include front-end measures to allow admin access only to admin.
  This is backed up in the back-end ensuring only these admin functions will run if
  admin is the sesson user.

  All other functions in the back-end are protected by ensuring that there is a sesson
  user for them to run, and only registered users would be logged in and set as sesson users.

<p align="center">Register Page</p>
<h2 align="center">
<img src="documentation/readme-images/reg1.png" width="50%">
</h2>

[Back to Table of Content](#table-of-content)

## User Base Page

  Once loged in the user is taken to their own User Base page which is the center base
  of the site and along with all other pages had a navbar to take them to any page.
  There they have access to the different departments to view each department's communications. 
  The core feature of the site is clarity and specificy. The first measure of this is the 
  seperating of the production communications into different departments.

  This page also allows the user to download the latest script and shotlist, to add messages 
  and provides a link to take them to the images page.

<p align="center">User Base Department Choices</p>
<h2 align="center">
<img src="documentation/readme-images/depts1.png" width="50%">
</h2>

[Back to Table of Content](#table-of-content)

## Departments Page

  Once the user clicks on a department they are taken to that department 
  Find by Date Page. That day's communications will automatically be displaying and the 
  user has the further options of finding all communications in that
  department or finding then by date.
  They can also click on a link to take them to the Find by Poster Page where they
  can find communications by entering the poster's name.

<p align="center">Department Page</p>
<h2 align="center">
<img src="documentation/readme-images/dep1.png" width="50%">
</h2>

[Back to Table of Content](#table-of-content)

## Images Page
    
  The user here can find images by entering a specific image tag name if they have 
  it or entering a search word relating to the images they wish to see. These image
  are only upload by admin so they are intended to be actual style and shooting choices,
  options of these or looks the creative team are going for. Here the admin can set images for users to know what choices
  have been made and what looks and themes are being uses In turn this is the means in which the user finds out what choices have been made, i.e. actual location
  images or colour themes, and therefore devise their own choices accordingly. 
  In posting options it also allows, along with the posting of images in the Departments 
  Page for discussion and collaboration.

<p align="center">Images Page</p>
<h2 align="center">
<img src="documentation/readme-images/hos1.png" width="50%">
</h2>

[Back to Table of Content](#table-of-content)

## Admin Page

  As discussed above in "decurity Measures" defensive programming will only allow
  access to the admin features if admin is the sesson user and this is inplemented
  both in the front-end and back-end. If the user is admin they will be given the 
  option to delete a user, upload the latest script, upload the latest shotlist 
  or upload new images.

<p align="center">Admin Page 1600px</p>
<h2 align="center">
<img src="documentation/readme-images/admin1.png" width="50%">
</h2>

<p align="center">Admin Page 375px</p>

<h2 align="center">
<img src="documentation/readme-images/admin2.png" width="25%">
</h2>

[Back to Table of Content](#table-of-content)

# Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)
- [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
- [JINJA](https://en.wikipedia.org/wiki/Jinja_(template_engine))

# Frameworks, Libraries & Programs Used

1. [Materialize:](https://materializecss.com/getting-started.html)
   - Materialize was used to create the overall framework and it's grid based 
     format for the site and it's primary responsiveness. Also specific 
     Materialize features were used throughout which include the, collapsable, 
     the navbar and sidenav, the modals, the tooltipped feature, the datepickers
     and the overall styling of the website.
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

[Back to Table of Content](#table-of-content)

# Testing

W3C Markup Validator, W3C CSS Validator. PEP8 and JSHint were used to validate every page of the project.

- [W3C Markup Validator](https://validator.w3.org/) - [Results](https://github.com/johnston9/MS3-Shot-Caller)
  - W3C "Direct Input" option was used on each html page. As Jinja was used throughout the site
    errors displayed where it was used on each page but no other error displayed.
    When I validated by URL no errors were shown as seen in the screenshot "W3C entire site by URL"

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

# Testing User Stories from User Experience (UX) Section

## First Time User Goals

1. As a First Time User, I want to learn what the site has to offer and how to use the site quickly.

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
    
<h2 align="center">
<img src="documentation/readme-images/user10.png" width="50%">
</h2>


2. As a First Time User, I want to find communications in my or other departments.

    1. Upon opening a department page the user will see the latest messages displayed.
       They will see the option to open all messages and a more specicic option
       to find messages by a particular date.
    2. The user will see a further option to go to "Find messages by Poster" and on clicking
       they will be taken to the "Find messages by Poster Page" where they can get all messages
       from a particular team member by typing in their full name as instructed.
    3. The user will see all chosen messages each displaying,in the header the name and position
       of the poster, the subject and whether it is a priority or not. On clicking on a message box
       it will open to show the message and an image if one has been posted.

<h2 align="center">
<img src="documentation/readme-images/dep-post.png" width="50%">
</h2>

3. As a First Time User, I want to view images.

    1. In the navbar and on their home base the user will see a link to search images
       which on clicking will take them to the images page.
    2. The user will see instruction on how to search for images. They can use a specicic
       image reference tag, if thet have one or they can input search words relevent
       to what they are looking for.
    3. The image bank is uploaded by the production team only so only contains sanctioned
       images of style choices, locations and other images all in keeping with the choices
       set by the team or different options that are being worked on or considered.

<p align="center">Specific reference tag input</p>
<h2 align="center">
<img src="documentation/readme-images/im-spec.png" width="50%">
</h2>

<p align="center">Specific reference tag result</p>
<h2 align="center">
<img src="documentation/readme-images/im-res1.png" width="50%">
</h2>

<p align="center">Result for query word "nick"</p>
<h2 align="center">
<img src="documentation/readme-images/im-word.png" width="25%">
</h2>

## Returning User Goals

4. As a Returning User, I want to download the latest shotlist and script.

    1. On clicking download script the script is downloaded to the user's device.

<p align="center">Result for downloaded script</p>
<h2 align="center">
<img src="documentation/readme-images/script1.png" width="50%">
</h2>

    1. On clicking download shotlist the shotlist is downloaded to the user's device.

<p align="center">Result for downloaded script</p>
<h2 align="center">
<img src="documentation/readme-images/shot1.png" width="50%">
</h2>


5. As a Returning User, I want to find messages in specific areas.

    1. Upon entering 
    2. Upon entering 
    3. Upon entering 

6. As a Returning User, I want to edit or delete my communications.

    1. Upon entering 
    2. Upon entering 
    3. Upon entering 

## Frequent User Goals

7. As a Frequent User, I want to view communications and see images relating to style, 
   shooting and script choices so I can develop my owm choices accordingly.

    1. Upon entering 
    2. Upon entering 
    3. Upon entering 

8. As a Frequent User, I want to post communications and images relating to my style, 
   shooting and script choices.

    1. Upon entering 
    2. Upon entering 
    3. Upon entering 

9. As a Frequent User, I want to collaborate with other user on specific areas of 
   production.

    1. Upon entering 
    2. Upon entering 
    3. Upon entering 

# Credits

[Back to Table of Content](#table-of-content)

# Code

- [W3schools.com](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp): Here I learnt how to create the return to top function.


[Back to Table of Content](#table-of-content)













