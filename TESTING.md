# OpenRent - Testing Plan

## Table of Contents

- [W3C HTML Validator](#w3c-html-validator)
- [W3C CSS Validator](#w3c-css-validator)
- [Google Lighthouse](#Google-lighthouse)
- [User Stories Testing](#user-stories-testing)
- [Manual Testing](#manual-testing)
  - [Testing plan](#testing-plan)
  - [Browser and Device Testing](#browser-and-device-testing)
  - [Bugs and Fixes](#bugs-and-fixes)
    - [Browser Bugs](#browser-bugs)
    - [General Bugs](#general-bugs)

## W3C HTML Validator

All HTML pages passed the W3C HTML validation with no errors.

## W3C CSS Validator

The CSS only returns an error related to the Materialize stylesheet. This app's custom CSS returns no error.

## Google Lighthouse

The app also passed the Google Lighthouse validation.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/google-lighthouse.png" width="400">

## CircleCI

Circle CI Continuous Integration was added to GitHub to make sure the app would still run after every commit.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/circle-ci-dashboard.png" width="500">

![Circle CI](https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/circle-ci-github.png)

## User Stories Testing

As a website user...

- I want to create an account.
  - _Goal achieved_: User clicks on "Log In" in the navbar or footer, then click "Sign Up Here". 
  
Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-register.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-register.png" width="250">

- I want to log in to my account.
  - _Goal achieved_: User clicks on "Log In" in the navbar or footer.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-login.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-login.png" width="250">

- I want to update my personal information
  - _Goal achieved_: User logs in, expands the heading "My Details" and clicks the "Edit Profile" button.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-edit-profile.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-edit-profile.png" width="250">

- I want to delete my account
  - _Goal achieved_: On my profile page, user expands heading "Privacy" and clicks the anchor link.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-delete-profile.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-delete-profile.png" width="250">

- I want to add a tenancy
  - _Goal achieved_: On my profile page, user expands heading "My Tenancies" and clicks the "Add Tenancy" button.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-add-tenancy.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-add-tenancy.png" width="250">

- I want to edit a tenancy
  - _Goal achieved_: Within the tenancy card under the "My Tenancies" heading, user clicks the "Edit Tenancy" button.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-edit-tenancy.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-edit-tenancy.png" width="250">

- I want to delete a tenancy
  - _Goal achieved_: Within the tenancy card under the "My Tenancies" heading, user clicks the "Delete Tenancy" button.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-delete-tenancy.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-delete-tenancy.png" width="250">

- I want to view the rent register map
  - _Goal achieved_: User navigates to "Rent Register" page and see the map with the markers.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-rent-register.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-rent-register.png" width="250">


- I want to be able to contact the rent register
  - _Goal achieved_: User navigates to Contact page.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-contact.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-contact.png" width="250">

## Manual Testing

The manual testing was conducted following the test plan below across different browsers and devices.

### Testing plan

Nav:
- [x] Make sure links are not broken and are linking to correct page.
- [x] Desktop: when user is logged in, navbar must display links Add Tenancy, Rent Register, User's Username.
- [x] Desktop: when hovering over username, dropdown must display with options: Profile, Log Out.
- [x] Mobile: when user is logged in, navbar must display links User's Username, Add Tenancy, Rent Register, Log Out.
- [x] Desktop and Mobile: When user is not logged in, navbar must display links Home, Rent Register, Contact Us, Log In.

Log In:
- [x] Type incorrect username and/or incorrect password and see an error message displayed.
- [x] Type correct username and password and land on profile page.
- [x] Click on "Sign up here" and land on Register page.

Sign Up:
- [x] Type passwords that don't match and see error message displayed.
- [x] Type username/password shorter than 5 characters and see error message displayed.
- [x] Type correct username and password and land on profile page.
- [x] Click on "Log in here" and land on Log in page.

Profile:
- [x] Click on the 3 headings and expand the accordion.
  
Edit Profile:
- [x] Expand heading "My Details", click on the button "Edit profile" and land on Edit Profile page.
- [x] Enter different first name, last name or email address and hit Edit Profile, see message "Profile successfully updated".
- [x] Return to profile page and see the different value inserted for first name, last name or email address.

Delete Profile:
- [x] Expand heading "Privacy" click on the link "click here" and see modal.
- [x] Within the modal, click cancel and return to profile.
- [x] Within the modal, click delete and note that you have been logged out and landed on index page.

Add Tenancy:
- [x] Expand heading "My Tenancies" click on the button "Add Tenancy" and land on Add Tenancy page.
- [x] Try to submit Tenancy without filling out the form and see error message.
- [x] In the Address Line 1 field, type address outside Dublin and see error message.
- [x] In the Address Line 1 field, type address within Dublin and move on.
- [x] Pick start date and inspect that dates which are less than 1 month from start date is grayed out in the end date field.
- [x] In the price field, an error message should display if characters other than dot, comma and numbers not ranging from 100 to 9999 are entered. 

Edit Tenancy:
- [x] Within the tenancy card, click on "Edit" and land on Edit Tenancy page.
- [x] On the Edit Tenancy page, the address of the tenancy clicked should be populated.
- [x] Change the value of an input and click on the button "Edit Tenancy", a success message should display.
- [x] If the change made is in the Address Line 1 field, type address outside Dublin and see error message.

Delete Tenancy:
- [x] Within the tenancy card, click on "Delete" and see modal.
- [x] Within the modal, click cancel and return to profile.
- [x] Within the modal, click delete and note that tenancy has been deleted from list.

Rent Register:
- [x] Click on the markers and see info window above the pin and tenancy card displayed below the map.

Footer:
- [x] Make sure links are not broken and link to correct pages.
- [x] When user is logged in, footer must display links Home, Rent Register, Contact Us.
- [x] When user is not logged in, footer must display links Home, Rent Register, Contact Us, Log In.

Contact Form:
- [x] Try to submit the empty form. Expect to see the error message underneath each required field.
- [x] Try to submit the form with an invalid email address. Expect to see an error message.
- [x] Try to submit the form with all inputs valid. Expect to see success message.

### Browser and Device Testing

The website was tested on the browsers and devices as follows. The website was not tested on a tablet as I do not have access to one.

| ID              | Device  | Browser                | OS                   | Compatibility |
| --------------- | ------- | ---------------------- | -------------------- | ------------- |
| D_Chrome_Win    | Desktop | Chrome 86.0            | Windows              |      |
| D_Firefox_Win   | Desktop | Firefox 79.0           | Windows              |      |
| D_Edge_Win      | Desktop | Microsoft Edge 44      | Windows              |           |
| D_IE_Win        | Desktop | Internet Explorer 11.1 | Windows              |            |
| D_Chrome_Linux  | Desktop | Chrome                 | Linux                |      |
| D_Firefox_Linux | Desktop | Firefox                | Linux                |      |
| D_Opera_Linux   | Desktop | Opera                  | Linux                |      |
| D_Chrome_Mac    | Desktop | Chrome                 | Mac                  |      |
| D_Firefox_Mac   | Desktop | Firefox                | Mac                  |      |
| D_Safari_Mac    | Desktop | Safari                 | Mac                  |           |
| M_Chrome_Sams   | Mobile  | Chrome                 | Samsung S8 Android 9 |      |
| M_Safari_iPhone | Mobile  | Safari                 | iPhone X             |           |
| M_Chrome_iPhone | Mobile  | Chrome                 | iPhone X             |           |

### Bugs and Fixes

A few bugs were encountered during the testing, which were addressed accordingly where possible.

#### Browser bugs

This section only highlights the browsers and devices in which compatibility are not excellent, referencing the ID as per table above. The bugs in this section were not fixed.


#### General bugs

