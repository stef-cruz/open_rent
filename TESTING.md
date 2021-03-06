# OpenRent - Testing Plan

## Table of Contents

- [W3C HTML Validator](#w3c-html-validator)
- [W3C CSS Validator](#w3c-css-validator)
- [JSHint Validator](#w3c-css-validator)
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

## JSHint

The JS code passed the JSHint validation with no major issues.

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
  - _Goal achieved_: On my profile page, user expands heading "Privacy" and clicks on the anchor link.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-delete-profile.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-delete-profile.png" width="250">

- I want to add a tenancy
  - _Goal achieved_: On my profile page, user expands heading "My Tenancies" and clicks on the "Add Tenancy" button.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-add-tenancy.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-add-tenancy.png" width="250">

- I want to edit a tenancy
  - _Goal achieved_: Within the tenancy card under the "My Tenancies" heading, user clicks on the "Edit Tenancy" button.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-edit-tenancy.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-edit-tenancy.png" width="250">

- I want to delete a tenancy
  - _Goal achieved_: Within the tenancy card under the "My Tenancies" heading, user clicks on the "Delete Tenancy" button.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-delete-tenancy.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-delete-tenancy.png" width="250">

- I want to view the rent register map
  - _Goal achieved_: User navigates to the "Rent Register" page and sees the map with the markers.

Desktop:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-desktop-rent-register.png" width="400">

Mobile:  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-mobile-rent-register.png" width="250">


- I want to be able to contact the rent register
  - _Goal achieved_: User navigates to the Contact page.

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
- [x] Desktop: when hovering over username, dropdown must display options Profile and Log Out.
- [x] Mobile: when user is logged in, navbar must display links User's Username, Add Tenancy, Rent Register and Log Out.
- [x] Desktop and Mobile: When user is not logged in, navbar must display links Home, Rent Register, Contact Us, Log In.

Log In:
- [x] Type incorrect username and/or incorrect password and see an error message displayed.
- [x] Type correct username and password and land on profile page.
- [x] Click on "Sign up here" and land on Register page.

Sign Up:
- [x] Type passwords that don't match and see error message displayed.
- [x] Type username/password shorter than 5 characters and see error message displayed.
- [x] Type correct username and password and land on profile page.
- [x] Click on "Log in here" and land on the Log in page.

Profile:
- [x] Click on the 3 headings and expand the accordion.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/profile and expect to see the 404 page.
  
Edit Profile:
- [x] Expand heading "My Details", click on the button "Edit profile" and land on Edit Profile page.
- [x] Enter different first name, last name or email address and hit Edit Profile, see message "Profile successfully updated" and return to profile page.
- [x] Expand heading "My Details" and see the different value inserted for first name, last name and/or email address.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/edit_profile and expect to see the 404 page.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/edit_profile/60412c99a3baf38b6b8ca989 (user ID) and redirect to login page.

Delete Profile:
- [x] Expand heading "Privacy" click on the link "click here" and see modal.
- [x] Within the modal, click cancel and return to profile.
- [x] Within the modal, click delete and note that you have been logged out and landed on the home page.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/delete_profile and expect to see the 404 page.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/edit_profile/60412c99a3baf38b6b8ca989 (user ID) and redirect to login page.

Add Tenancy:
- [x] Expand heading "My Tenancies" click on the button "Add Tenancy" and land on Add Tenancy page.
- [x] Try to submit Tenancy without filling out the form and see error message.
- [x] In the Address Line 1 field, type address outside Dublin, click on "Add Tenancy" button and see error message.
- [x] In the Address Line 1 field, type address within Dublin, click on "Add Tenancy" button and move on.
- [x] Pick start date and when selecting end date, inspect that dates which are less than 1 month from start date are grayed out.
- [x] In the price field, an error message should display if characters other than dot, comma and numbers not ranging from 100 to 9999 are entered. 
- [x] Try to access the url http://ci-milestone3.herokuapp.com/add_tenancy and redirect to login page.

Edit Tenancy:
- [x] Within the tenancy card, click on "Edit" and land on Edit Tenancy page.
- [x] On the Edit Tenancy page, the address of the tenancy clicked should be populated.
- [x] Change the value of an input and click on the button "Edit Tenancy", a success message should display.
- [x] If the change made is in the Address Line 1 field, type address outside Dublin, hit "Edit Tenancy" and see error message.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/edit_tenancy and expect to see the 404 page.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/edit_tenancy/60412d6da3baf38b6b8ca98a (tenancy ID) and redirect to login page.

Delete Tenancy:
- [x] Within the tenancy card, click on "Delete" and see modal.
- [x] Within the modal, click cancel and return to profile.
- [x] Within the modal, click delete and note that tenancy has been deleted from list.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/delete_tenancy and expect to see the 404 page.
- [x] Try to access the url http://ci-milestone3.herokuapp.com/delete_tenancy/60412d6da3baf38b6b8ca98a (tenancy ID) and redirect to login page.

Rent Register:
- [x] Click on the markers and see info window above the pin and tenancy card displayed below the map.

Footer:
- [x] Make sure links are not broken and link to correct pages.
- [x] When user is logged in, footer must display links Home, Rent Register, Contact Us.
- [x] When user is not logged in, footer must display links Home, Rent Register, Contact Us, Log In.

Contact Form:
- [x] Try to submit the empty form. Expect to see the error message underneath the required fields.
- [x] Try to submit the form with an invalid email address. Expect to see an error message.
- [x] Try to submit the form with all inputs valid. Expect to see success message.

### Browser and Device Testing

The website was tested on the browsers and devices as follows. Unfortunately I do not have access to a tablet so the website on this device.

| ID              | Device  | Browser                | OS                   | Compatibility |
| --------------- | ------- | ---------------------- | -------------------- | ------------- |
| D_Chrome_Win    | Desktop | Chrome 86.0            | Windows              |  Excellent    |
| D_Firefox_Win   | Desktop | Firefox 79.0           | Windows              |  Excellent    |
| D_Edge_Win      | Desktop | Microsoft Edge 44      | Windows              |  Excellent    |
| D_IE_Win        | Desktop | Internet Explorer 11.1 | Windows              |  Good         |
| D_Chrome_Linux  | Desktop | Chrome                 | Linux                |  Excellent    |
| D_Firefox_Linux | Desktop | Firefox                | Linux                |  Excellent    |
| D_Opera_Linux   | Desktop | Opera                  | Linux                |  Excellent    |
| D_Chrome_Mac    | Desktop | Chrome                 | Mac                  |  Excellent    |
| D_Firefox_Mac   | Desktop | Firefox                | Mac                  |  Excellent    |
| D_Safari_Mac    | Desktop | Safari                 | Mac                  |  Excellent    |
| M_Chrome_Sams   | Mobile  | Chrome                 | Samsung S8 Android 9 |  Excellent    |
| M_Safari_iPhone | Mobile  | Safari                 | iPhone 6             |  Excellent    |
| M_Chrome_iPhone | Mobile  | Chrome                 | iPhone 6             |  Excellent     |
| M_Chrome_iPhone | Mobile  | Chrome                 | iPhone X             |  Excellent     |

### Bugs and Fixes

A few bugs were encountered during the testing, which were addressed accordingly where possible.

#### Browser specific bugs

This section only highlights the browsers and devices in which compatibility are not excellent, referencing the ID as per table above. The only bug fixed in this section was the CSS applied to the button "Edit Profile" on Safari for both mobile and desktop.

- D_IE_Win
  - Add Tenancy button does not work. It does not bring user back to profile page as expected.
  - Duration of tenancy javascript function does not work. Field is blank.
  
<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-ie-windows-2.png" width="400">

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-ie-windows.png" width="400">

- D_Safari_Mac
  - Button "Edit Profile" did not have CSS applied, which was corrected by removing the submit type from the button.

<img src="https://github.com/stefcruz/ci_milestone3/blob/master/app/static/images/testing_md/testing-safari-edit-profile.png" width="400">

#### General bugs

- When user is logged in and navigates to page http://ci-milestone3.herokuapp.com/login and http://ci-milestone3.herokuapp.com/register, error message was being displayed. This was corrected to show 404 page instead.