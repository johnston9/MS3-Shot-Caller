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


<h2 align="center">User Experience (UX)</h2>

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


### User stories

 - #### First Time User Goals

1. As a First Time User, I want to learn what the site has to offer and how to use the site quickly.
2. As a First Time User, I want to find and add communications in my department.
3. As a First Time User, I want to upload and view images.

  - #### Returning User Goals

4. As a Returning User, I want to download the latest shotlist and script
5. As a Returning User, I want to find messages in specific areas.
6. As a Returning User, I want to edit or delete my communications.

  - #### Frequent User Goals

7. As a Frequent User, I want to view communications and see images relating to style, 
   shooting and script choices so I can develop my owm choices accordingly.
8. As a Frequent User, I want to post communications and images relating to my style, 
   shooting and script choices.
9. As a Frequent User, I want to collaborate with other user on specific areas of 
   production.

<h2 align="center">Design</h2>

---

<h2 align="center">
<img src="documentation/readme-images/log1.png" width="90%">
</h2>

  - #### Colour Scheme
    - The site aims to be minimal streamlined and slick using an offblack background 
      colour with blue side image panels and an offwhite text. Crimson and blue tones
      are used minimally against this for a touch of sophisticated flare especially
      the site title in crimson letters running downwards on either side of the header box.

  
  - #### Typography
    - Materialize was used for the site and I kept their inherent font-family style 
      choice with was: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, 
      Oxygen-Sans, Ubuntu,Cantarell, "Helvetica Neue", sans-serif. This worked perfectly
      for the style of the site.


  - #### Imagery
    - The site was designed to have a minimal straight to business slick slightly cinematic look. This was achieved
      by the use of right and reversed left narrow side panels on an offblack background.
      The panels contain an images of a narrow window and it's blue lighting
      effect which act as a foreground to the complementing seemingly distant dark header box
      container which also has one of the images to which focus is drawn. The hope is that
      this achieves a feeling of cinematic lighting and depth.

  - #### Wireframes

    - PDF – Balsamic was used to design the layout for login, register, user base, 
      dep messages, images, and the add and admin upload pages.

- [View on Github](https://github.com/johnston9/MS3-Shot-Caller)

<h2 align="center">Features</h2>

### Existing Features

- #### Responsive Design

  The site is responsive to all sizes and the images remain whole and in proportion at all sizes.

---

<h2 align="center">
<img src="documentation/readme-images/post-16.png" width="50%">
</h2>

<p align="center"> Large Screen 1600px</p>
---

<h2 align="center">
<img src="documentation/readme-images/post-md.png" width="50%">
</h2>

<p align="center">  Medium Screen 1000px</p>
---

<h2 align="center">
<img src="documentation/readme-images/post-sm.png" width="25%">
</h2>

<p align="center"> Small Screen 370px</p>

- #### Login/Register Pages and Security Measures

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

---
<h2 align="center">
<img src="documentation/readme-images/reg1.png" width="50%">
</h2>

<p align="center">Register Page</p>

- #### User Base Page

  Once loged in the user is taken to their own User Base page which is the center base
  of the site and along with all other pages had a navbar to take them to any page.
  There they have access to the different departments to view each department's communications. 
  The core feature of the site is clarity and specificy. The first measure of this is the 
  seperating of the production communications into different departments.

  This page also allows the user to download the latest script and shotlist, to add messages 
  and provides a link to take them to the images page.

---
<h2 align="center">
<img src="documentation/readme-images/depts1.png" width="50%">
</h2>

<p align="center">User Base Department Choices</p>

  - #### Departments Page

  Once the user clicks on a department they are taken to that department 
  Find by Date Page. That day's communications will automatically be displaying and the 
  user has the further options of finding all communications in that
  department or finding then by date.
  They can also click on a link to take them to the Find by Poster Page where they
  can find communications by entering the poster's name.

---
<h2 align="center">
<img src="documentation/readme-images/dep1.png" width="50%">
</h2>

<p align="center">Department Page</p>

  - #### Images Page
    
    The user here can find images by entering a specific image tag name if they have 
    it or entering a search word relating to the images they wish to see. These image
    are only upload by admin so they are intended to be actual style and shooting choices,
    options of these or looks the creative team are going for. Here the admin can set images for users to know what choices
    have been made and what looks and themes are being uses In turn this is the means in which the user finds out what choices have been made, i.e. actual location
    images or colour themes, and therefore devise their own choices accordingly. 
    In posting options it also allows, along with the posting of images in the Departments 
    Page for discussion and collaboration.

---
<h2 align="center">
<img src="documentation/readme-images/hos1.png" width="50%">
</h2>

<p align="center">Images Page</p>

  - #### Admin Page

    If the user is admin they will be given the option to delete a user, upload the 
    latest script, upload the latest shotlist or upload new images.

---
<h2 align="center">
<img src="documentation/readme-images/admin1.png" width="50%">
</h2>

<p align="center">Admin Page 1600px</p>

---
  - This is also fully responsive.

<h2 align="center">
<img src="documentation/readme-images/admin2.png" width="50%">
</h2>

<p align="center">Admin Page 375px</p>




















