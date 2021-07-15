## Description

# Front-End: 

Vue3 

## Pages

#### Frontpage

Not a priority until funcitonality is completed. Just need a landing page to highlight the functionality of the app. 

Nav with site title, Sign In and Sign Up

#### Login

Doesnt need to be anything fany. Just a form for user/pass + submit button

#### Collections

Primary Dashboard when signed in. Will list all existing Collections as cards. Each card will have the Collection name, description and number of cards. Each card should have a heart button in the top right to favorite. 

Edit and Delete options in bottom right corner. 

Card outline with option add new collection

Navigation option to select collections. Selected items will have the following options
* Favorite
* Delete

#### Collection

- Card List
- Each card has: 
    * Favorite
    * Edit
    * Delete
- Card Add
- Highlight favorite
- Select
    - Quiz
    - Copy
    - Delete
- Quiz Button
    - If some are selected, quiz with selected
    - If none are selected, Quiz All


#### Profile

Will require authentication and models for users. 

#### Quiz

- Shuffle button
- Return to default button
- Next/Back




# Back-End

Django

to-do

# Database

SQLite

## Models

#### User

* User ID
* User name
* Password
* Created Date

#### Collection

* Collection ID
* Collection Title
* Collection Description
* Collection color
* Created Date
* is_active
* is_favorite

#### Card

* Card ID
* Created Date
* Card header
* Card body
* is_favorite





