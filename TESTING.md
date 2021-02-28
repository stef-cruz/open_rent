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

All HTML pages have passed the W3C HTML validation.

## W3C CSS Validator

The CSS only returns an error related to the Materialize stylesheet. This app's custom CSS returns no error.

## Google Lighthouse


<img src="https://github.com/stefcruz/ci_milestone2/blob/master/readme/testing/lighthouse.png" width="400">

## CircleCI Continuous Integration


## User Stories Testing

- I want to create an account  
  
Desktop:
  
Mobile:

- I want to update my personal information
- I want to delete my account
- I want to add a tenancy
- I want to delete a tenancy
- I want to edit a tenancy
- I want to view the rent register map
- I want to be able to contact the rent register

## Manual Testing

The manual testing was conducted following the test plan below across different browsers and devices.

### Testing plan

Nav:

- [x] Make sure links are not broken and are linking to correct page.
- [x] Scroll down and see the arrow up coming up on the right hand side of the screen.
- [x] Click on arrow up to bring to top.

Main section:

- [x] Search for an ingredient and dish pressing enter.
- [x] Search for an ingredient and dish pressing the search button.
- [x] Perform search ticking one, two, three and four checkboxes.
- [x] Click on clear icon to clear contents of search bar.
- [x] Click on link "See Recipe" on recipe card.

Inspiration section:

- [x] Use arrows to navigate through the recipe cards.
- [x] Click on link "See Recipe" on recipe card.

Nutritional value:

- [x] Enter ingredient list with expected values and perform search pressing enter. It was working as expected however had to remove this feature. Explanation in the Bugs & Fixes section.
- [x] Enter ingredient list with expected values and perform search pressing search button.
- [x] Enter ingredient list missing one of the required search term (either missing the unit or measure). Expect to see the error message mentioned above in the [Existing Features](#error-handling-nutritional-value) section.

Footer:

- [x] Click on nav links in the footer.
- [x] Click on social media links.

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

#### General bugs
