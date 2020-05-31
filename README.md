# Project 1

Web Programming with Python and JavaScript

## Getting Started

### Prerequisites

**Step 1** Install [Python](https://www.python.org/downloads/). You should be using Python version 3.6 or higher.

**Step 2**, Install [pip](https://pip.pypa.io/en/stable/installing/). If you downloaded Python from Python’s website, you likely already have pip installed (you can check by running pip in a terminal window). Make sure it's pip3.

**Step 3** Run `pip3 install -r requirements.txt` in your terminal window to make sure that all of the necessary Python packages (Flask and SQLAlchemy, for instance) are installed.

**Step 4** Install [PostgreSQL](https://www.postgresql.org/download/)

**Step 5** Set the environment variable FLASK_APP to be application.py. On a Mac or on Linux, the command to do this is export FLASK_APP=application.py. On Windows, the command is instead set FLASK_APP=application.py. You may optionally want to set the environment variable FLASK_DEBUG to 1, which will activate Flask’s debugger and will automatically reload your web application whenever you save a change to a file.

**Step 6** Set the environment variable DATABASE_URL to be the URI of your database, which you should be able to see from the credentials page on Heroku.

Run `flask run` to start up the application.

## Deployment

## Built With

- Flask
- Bootstrap
- SASS
- CSS
- HTML5

## User Story

AAU, I want to sign up with a username, password and email address.
AAU, I want to login with username and password that I registered with. If the password/username is wrong or doesn't match. It should render a error message.
AAU, I want search for a book by isbn, title or author. If the query is empty or there is not found in our database. It should render a message.
AAU, I want rating and write a review for a book but I can't submit multiple comment for one book.

## Files

### Contents of Each File

#### book.html

It shows book details, including book author, book title, book isbn, publish year and recent reviews for this book from our users.
It also includes average ratings and review count that pull off from goodreads API. and review form which you can submit a review with rating.

#### books.html

It shows 50 books from our website. You have to login in to view this page, otherwise, you will be redirect to Login page.

#### error.html

Render error message accordingly.

#### home.html

A hero page which contents a link of first 50 books in our database.

#### layout.html

A layout templates which include a nav bar and all needed scripts

#### login.html

Form for login

#### result.html

Book search results with book details such as Title Author, Year, isbn and Published year on cards.

#### sign_up.html

Form for sign up
