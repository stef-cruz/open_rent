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
     * [Tenancy card](#tenancy-card)
     * [Contact page](#contact-page)
  - [Features Left to Implement](#features-left-to-implement)

</details>

<details>
  <summary>Technologies</summary>

  - [Technologies Section](#technologies-section)
  - [Programming Languages](#programming-languages)
  - [Other Tools](#other-tools)

</details>

<details>
  <summary>Testing</summary>

  - [Testing Documentation](#testing-documentaion)
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
- I want to be able to contact the register

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
│   ├── init.py
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
│   │   ├── rent-register.html
│   │   └── view-tenancy.html
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
![Nav mobile and tablet](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-mobile-tablet.png)

![Nav mobile sidenav](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-mobile-sidenav.png)

Favicon:  
![Nav favicon](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-favicon.png)

When logged in, the user can hover over their username and they can log out or go to profile page.

![Nav username hover](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/nav-username-hover.png)

#### Home page

The content on the home page looks the same for registered and unregistered users, except the call to action on the "How does it work?" section.

Registered user:  
![Home page registered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/home-page-cta-registered-user.png)

Unregistered user:  
![Home page unregistered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/home-page-cta-unregistered-user.png)


#### Footer

The footer has links to the sections of the homepage and also social media. Different links are displayed when the user is logged in.

Desktop & mobile unregistered user:  
![Desktop footer unregistered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-desktop-unreg-user.png)

![Mobile footer unregistered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-mobile-unreg-user.png)

Desktop & mobile registered user:  
![Desktop footer registered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-desktop-reg-user.png)

![Mobile footer registered user](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/footer-mobile-reg-user.png)

#### Log in

Users can log in to the app by typing their combination of username and password, which is validated by the Flask app and will throw an error in case of unmatch. All passwords are hashed. Users can create an account by  clicking on "sign up here".

![Log in](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/log-in.png)

#### Sign up

The sign up is a simple solution where only username and password is required. The password is verified twice to ensure they match before signing user in and writing to the database.

![Sign up](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/sign-up.png)

#### Profile page

The profile page uses the Materialize accordion, which is collasped when the user first land on this page. The sections expand when clicking and reveal the user's details, tenancies uploaded and the option to delete the profile under the privacy heading.

Accordion collapsed:  
![Profile page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-desktop.png)

My details:  
![My details profile page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-my-details.png)

My Tenancies:  
![My tenancies profile page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-my-tenancies.png)

Privacy:  
![Privacy profile page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/profile-privacy.png)

#### Edit profile

Within the profile page, the user has the ability to edit their personal information such as first name, last name and email address.

![Edit profile](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/edit-profile.png)

#### Delete profile

The option to delete the profile sits under the privacy tab, where the user is prompted with the option to delete profile or cancel action.

![Delete profile](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/delete-profile.png)

#### Add tenancy

Users can add a tenancy by clicking the button add tenancy on their profile, which will be plotted in a map on the Rent Register page.

![Add tenancy page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy.png)

The Address Line 1 field is hooked up to Google Maps Autocomplete address, which triggers once user starts typing. It is configured to allow addresses from Dublin only.

![Add tenancy google maps autocomplete](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy-google-maps-autocomplete.png)

The user also has to select the start and end date for the tenancy, which utilises the Materialize Date Picker. 

![Add tenancy date picker](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy-date-picker.png)

All the fields in the form are validated, example below for the price where only numbers, dots, commas and numbers can be entered. The date is also validated, not allowing users to insert a tenancy of less than 1 month.

![Add tenancy form validation](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/add-tenancy-form-validation.png)

#### Edit tenancy

Once a tenancy is inserted, the user can edit the tenancy and the same validation of address, date and  apply. 

![Edit tenancy](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/edit-tenancy.png)

![Edit tenancy page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/edit-tenancy-page.png)

#### Delete tenancy

The tenancy can be deleted by clicking the delete button from the profile page. User will be prompted with a modal to confirm the action.

![Delete tenancy](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/delete-tenancy.png)

#### Rent register page

The rent register page shows Google Maps with markers which are the tenancies added by the users.

![Rent register page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/rent-register-page.png)

Clicking on the marker opens up an info window and a card underneath the map with the tenancy details.

![Rent register info window](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/rent-register-page-tenancy-card.png)

#### Contact page

The contact form contains a simple form with name, surname, email address and a message. EmailJS was used to enable this page to send emails.

![Contact page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/contact-page.png)

#### Error pages

The application displays custom error pages when something goes wrong.

![Error page](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/readme_md/404-page.png)

### Features Left to Implement

If it was not for the time constraint, this application could have had the following features:

- Log in with email address instead of username and email verification
- Option to see all tenancies on a page, where user could search, sort and filter results
- Ability to export the data from the website that could allow for manipulation of results in Excel, for example
- Dashboard page displaying all tenancies and various different graphs