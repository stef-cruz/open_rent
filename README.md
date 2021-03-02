# OpenRent - Rent Register Dublin



## Overview

[OpenRent](http://ci-milestone3.herokuapp.com/) is a Rent Register for Dublin. Users can insert the tenancy and then rent amount. The objective is to deliver a service to society which will aid in the fight for illegal rent increases. This public register can also help identifying pressure zones with accurate and up to date information.



## Table of Contents

<details>
  <summary>UX</summary>

  - [UX section](#ux-section)  
  - [User stories](#user-stories)  
  - [Wireframes](#wireframes)  
</details>

<details>
  <summary>Features</summary>

  - [Features Section](#features-section)
  - [Existing Features](#existing-features)
     * [App structure](#app-structure)
     * [Navigation bar](#navigation-bar)
     * [Home page](#recipe-cards)
     * [Footer](#footer)
     * [Log in](#log-in)
     * [Sign up](#sign-up)
     * [Profile page](#profile-page)
     * [Edit profile](#edit-profile)
     * [Delete profile](#delete-profile)
     * [Add tenancy](#add-tenancy)
     * [Edit tenancy](#edit-tenancy)
     * [Delete tenancy](#delete-tenancy)
     * [Rent register page](#rent-register-page)
     * [Contact page](#contact-page)
     * [Error pages](#error-pages)
  - [Features Left to Implement](#features-left-to-implement)

</details>

<details>
  <summary>Database Schema</summary>

- [Database Schema](#database-schema)

</details>

<details>
  <summary>Technologies</summary>

  - [Technologies Section](#technologies-section)
  - [Programming Languages](#programming-languages)
  - [Other Tools](#other-tools)

</details>

<details>
  <summary>Testing</summary>

  - [Testing Documentation](https://github.com/stefcruz/ci_milestone3/blob/master/TESTING.md)
</details>

<details>
  <summary>Deployment</summary>

  - [How to deploy to Heroku](#how-to-publish-to-heroku)
  - [How to fork this repository](#how-to-fork-this-repository)
  - [How to open this project locally](#how-to-open-this-project-locally)
</details>

<details>
  <summary>Credits</summary>

  - [Credits section](#credits-section)
  - [Content](#content)
  - [Images](#images)
</details>

<details>
  <summary>Acknowledgements</summary>

  - [Acknowledgements section](#acknowledgements-section)
  - [Design](#design)
  - [Code](#code)
</details>



## UX

### User stories

As the rent register user...

- I want to create an account
- I want to update my personal information
- I want to delete my account
- I want to add a tenancy
- I want to delete a tenancy
- I want to edit a tenancy
- I want to view the rent register map
- I want to be able to contact the rent register

### Wireframes

The wireframes for this project can be seen [here](https://www.figma.com/file/PPwrIzS5G1zAT0bHKw8x70/milestone_3?node-id=0%3A1).

[![img](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/wireframes.png)](https://www.figma.com/file/PPwrIzS5G1zAT0bHKw8x70/milestone_3?node-id=0%3A1)

## Features

### Existing Features

#### App structure

Following the package method from [this Pythonise tutorial](https://pythonise.com/series/learning-flask/flask-application-structure), the application is structured as a package and was imported within the different python files. This strategy allows for scale and maintains the files organised.

```bash
.
├── app
│   ├── contact.py
│   ├── database.py
│   ├── errors.py
│   ├── __init__.py
│   ├── login.py
│   ├── profile.py
│   ├── tenancy.py
│   └── views.py
│   ├── static
│   │   ├── css
│   │   │   ├── _card-tenancy.scss
│   │   │   ├── _contact.scss
│   │   │   ├── _divider.scss
│   │   │   ├── _edit-profile.scss
│   │   │   ├── _errors.scss
│   │   │   ├── _footer.scss
│   │   │   ├── _index.scss
│   │   │   ├── _nav.scss
│   │   │   ├── _profile.scss
│   │   │   ├── _register.scss
│   │   │   ├── _rent-register.scss
│   │   │   ├── style.css
│   │   │   ├── style.css.map
│   │   │   ├── style.scss
│   │   │   ├── _tenancy.scss
│   │   │   └── _variables.scss
│   │   ├── images
│   │   │   ├── 404-not-found.png
│   │   │   ├── 500-server-error.png
│   │   │   ├── arrow.png
│   │   │   ├── favicon.ico
│   │   │   ├── for-the-community-boy.png
│   │   │   ├── for-the-community-girl.png
│   │   │   ├── for-you.png
│   │   │   ├── icons8-circled-1.png
│   │   │   ├── icons8-circled-2.png
│   │   │   ├── icons8-circled-3.png
│   │   │   ├── icons8-country-house.png
│   │   │   ├── icons8-ireland-map.png
│   │   │   ├── icons8-money-bag.png
│   │   │   ├── readme_md
│   │   │   │   └── wireframes.png
│   │   │   ├── testing_md
│   │   │   └── woman-in-house.png
│   │   └── js
│   │       ├── displayTenancy.js
│   │       ├── durationOfTenancyProfile.js
│   │       ├── durationOfTenancyRentRegister.js
│   │       ├── email.js
│   │       ├── mapAutoComplete.js
│   │       ├── map.js
│   │       ├── materialize.js
│   │       ├── selectInputValidation.js
│   │       └── startEndDateTenancy.js
│   ├── templates
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── add-tenancy.html
│   │   ├── base.html
│   │   ├── contact.html
│   │   ├── edit-profile.html
│   │   ├── edit-tenancy.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── register.html
│   │   └──  rent-register.html
├── README.md
├── requirements.txt
└──  run.py
```


#### Navigation bar

The navbar contains links to the different sections of the site and collapses when the user accesses the website through mobile. The nav also displays the username for users who are logged in on all devices.

Nav desktop:  
![Nav desktop registered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-desktop-registered-user.png)

![Nav desktop unregistered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-desktop-unregistered-user.png)

Nav mobile and tablet:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-mobile-tablet.png" width="250">

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-mobile-sidenav.png" width="250">

Favicon:  
![Nav favicon](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-favicon.png)

When logged in, the user can hover over their username and they can log out or go to profile page.

![Nav username hover](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-username-hover.png)

#### Home page

The content on the home page looks the same for registered and unregistered users, except the call to action on the "How does it work?" section.

Registered user:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/home-page-cta-registered-user.png" width="450">

Unregistered user:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/home-page-cta-unregistered-user.png" width="450">

#### Footer

The footer has links to the sections of the homepage and also social media. Different links are displayed when the user is logged in.

Desktop & mobile unregistered user:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-desktop-unreg-user.png" width="450">

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-mobile-unreg-user.png" width="250">

Desktop & mobile registered user:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-desktop-reg-user.png" width="450">

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-mobile-reg-user.png" width="250">


#### Log in

Users can log in to the app by typing their combination of username and password, which is validated by the Flask app and will throw an error in case of unmatch. All passwords are hashed. Users can create an account by  clicking on "sign up here".

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/log-in.png" width="400">

#### Sign up

The sign up is a simple solution where only username and password is required. The password is verified twice to ensure they match before signing user in and writing to the database.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/sign-up.png" width="400">

#### Profile page

The profile page uses the Materialize accordion, which is collasped when the user first land on this page. The sections expand when clicking and reveal the user's details, tenancies uploaded and the option to delete the profile under the privacy heading.

Accordion collapsed:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-desktop.png" width="400">

My details:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-my-details.png" width="400">

My Tenancies:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-my-tenancies.png" width="400">

Privacy:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-privacy.png" width="400">

#### Edit profile

Within the profile page, the user has the ability to edit their personal information such as first name, last name and email address.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/edit-profile.png" width="400">

#### Delete profile

The option to delete the profile sits under the privacy tab, where the user is prompted with the option to delete profile or cancel action.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/delete-profile.png" width="400">

#### Add tenancy

Users can add a tenancy by clicking the button add tenancy on their profile, which will be plotted in a map on the Rent Register page.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy.png" width="400">

The Address Line 1 field is hooked up to Google Maps Autocomplete address, which triggers once user starts typing. It is configured to allow addresses from Dublin only.

![Add tenancy google maps autocomplete](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy-google-maps-autocomplete.png)

The user also has to select the start and end date for the tenancy, which utilises the Materialize Date Picker. 

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy-date-picker.png" width="300">

All the fields in the form are validated, example below for the price where only numbers, dots, commas and numbers can be entered. The date is also validated, not allowing users to insert a tenancy of less than 1 month.

![Add tenancy form validation](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy-form-validation.png)

#### Edit tenancy

Once a tenancy is inserted, the user can edit the tenancy and the same validation of address, date and  apply. 

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/edit-tenancy.png" width="400">

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/edit-tenancy-page.png" width="400">

#### Delete tenancy

The tenancy can be deleted by clicking the delete button from the profile page. User will be prompted with a modal to confirm the action.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/delete-tenancy.png" width="400">

#### Rent register page

The rent register page shows Google Maps with markers which are the tenancies added by the users.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/rent-register-page.png" width="400">

Clicking on the marker opens up an info window and a card underneath the map with the tenancy details.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/rent-register-page-tenancy-card.png" width="400">

#### Contact page

The contact form contains a simple form with name, surname, email address and a message. EmailJS was used to enable this page to send emails.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/contact-page.png" width="400">

#### Error pages

The application displays custom error pages when something goes wrong.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/404-page.png" width="400">

### Features Left to Implement

If it was not for the time constraint, this application could have had the following features:

- Log in with email address instead of username and email verification
- Option to see all tenancies on a page, where user could search, sort and filter results
- Ability to export the data from the website that could allow for manipulation of results in Excel, for example
- Dashboard page displaying all tenancies and various different graphs
- Automated unit tests

## Database Schema

The database has three collections and follows the structure below.

Accommodation Types collection:

``{``  
``"_id":                  <ObjectID>,``  
``"accommodation_type":    <string>``  
``}``

Tenancies collection:

``{``  
``"_id": <ObjectID>,``  
``"address_1": <string>``  
``"address_2": <string>``  
``"latitude": <double>``  
``"longitude": <double>``  
``"accommodation_type": <string>``  
``"start_date": <string>``  
``"end_date": <string>``  
``"price": <string>``  
``}``  

Users collection:

``{``  
``"_id": <ObjectID>,``  
``"username": <string>``  
``"password": <string>``  
``"email_address": <double>``  
``"first_name": <double>``  
``"last_name": <double>``  
``}``  

## Technologies

### Programming Languages

- Flask  
  Main framework for this application.
- Python  
  Back end & data manipulation.
- Jinja  
  Templating language for template manipulation.
- MongoDB  
  Non-relational database used in this application.
- HTML5  
  Markup language used across the app.
- CSS3  
  Page style.
- JavaScript  
  Front end functionalities & API calls.
- SASS  
  CSS preprocessor.
- Materialize  
  This project used Materialize design elements such as navbar, grid & cards.

### Other Tools

- GitHub  
  Used to store this project's source code.
- Heroku  
  Used to host this app.
- WebStorm  
  IDE used to write HTML, SASS and Jinja.
- Pycharm  
  IDE used to write Python.
- Figma  
  Creation of wireframes.
- [Email JS](https://www.emailjs.com/)  
  Tool used to send emails from JS.

## Testing

Testing documentation is available [here](https://github.com/stefcruz/ci_milestone3/blob/master/TESTING.md).

## Deployment

This project's source code is hosted on GitHub and deployed to Heroku. It was created using WebStorm and Pycharm IDEs.

A clone of this repository was made locally, and the changes were deployed directly in the master branch. The commands used to push the changes were `git add .`, `git commit -m "message"` and `git push`. All the commits can be clearly identified by a concise and meaningful message.

### How to deploy to Heroku

There are two ways to deploy to Heroku. One is installing Heroku on your project and push changes to Heroku and the other is setting the automatic deployment from GitHub, which is easier.

Both require the creation of the app on Heroku website or through the CLI (instructions [here](https://devcenter.heroku.com/articles/creating-apps)).

Enabling automatic deployment from GitHub:

1. Create requirements.txt file so Heroku knows which dependencies to install. To create one ``pip3 freeze --local > requirements.txt``
2. Create procfile echo web: ``python run.py > Procfile``, then push requirements and procfile to git
3. Create the app on Heroku website
4. If your project uses any keys hidden in the gitignore file, go to Heroku and add them there in Settings > Config Vars
5. Go to Deploy > connect the repo name > enable automatic deploy from master branch > go to the next section ‘Manual Deploy’ and click on ‘Deploy Branch’

Installing Heroku on your project:
1. Create app on Heroku website
2. Make sure your project has requirements.txt file so Heroku knows which dependencies to install. To create one ``pip3 freeze --local > requirements.txt``
3. Install Heroku on your project ``npm install -g heroku``
4. Before pushing to Heroku, use the command git remote -v and see that only github links are listed
5. Add your project to heroku with the command ``git remote add heroku project-link``. Project link can be found at your Heroku app > Settings > Heroku git URL
7. Push to heroku ``git push -u heroku master``
8. Create procfile ``echo web: python run.py > Procfile``, then ``git add -A``, ``git commit -m "Add Procfile"``, ``git push``
9. If your project uses any keys hidden in the gitignore file, go to Heroku and add them there in Settings > Config Vars

More information about deploying with Git [here](https://devcenter.heroku.com/articles/git).

### How to fork this repository

If you would like to experiment with this project without changing it, follow the steps below.

1. After logging into your GitHub account, open up [this GitHub repository](https://stefcruz.github.io/ci_milestone3/)
2. Click on the 'Fork' button at the top right-hand corner of the page
3. Start coding!

### How to open this project locally

There are two options to clone this project to your local machine, using the command line and using GitHub desktop. Both are detailed [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

#### Using the command line

1. Go to the main page of [this GitHub repository](https://github.com/stefcruz/ci_milestone3).
2. Click on 'Code'.
3. First select whether you want to clone this repo using HTTPS, SSH or CLI, then click on the clipboard icon.
4. Open Terminal on your computer or the terminal from your IDE.
5. Change the current working directory to the location where you want the directory to be cloned.
6. Type `git clone`, and then paste the URL you copied earlier.
   ```shell
   $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
   ```
7. Press Enter to create your local clone.

#### Using GitHub Desktop

1. Go to the main page of [this GitHub repository](https://github.com/stefcruz/ci_milestone3).
2. Click on 'Code'.
3. Click 'Open with GitHub Desktop'.
4. Click  'Choose...' and select the location where you want to save this repo on your machine.
5. Open the project on your favourite IDE.

More information can be found [here](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/cloning-a-repository-from-github-to-github-desktop).

## Credits

### Images
- [Illustrations](https://icons8.com/illustrations/style--pablita)
- [Icons](http://icons8.com/)

## Acknowledgements

### Design
- [Colour theme and home page inspiration](https://www.squadeasy.com/en/)

### Code
- [App Structure](https://pythonise.com/series/learning-flask)
- [Extract lat and long from geocode_result](https://stackoverflow.com/questions/37311687/extracting-lat-lon-from-geocode-result-list-with-python-google-maps-api)
- [Google Maps Services Python](https://github.com/googlemaps/google-maps-services-python)
- [JS used to calculate duration of tenancy](https://stackoverflow.com/questions/2536379/difference-in-months-between-two-dates-in-javascript)
- [JS ensure infoWindow closes every time a new marker is clicked](https://stackoverflow.com/questions/12621274/close-infowindow-when-another-marker-is-clicked)
- [JS user cannot select end date of tenancy that is less than 1 month from start date](https://codepen.io/luv2code/pen/oNvrWyZ)