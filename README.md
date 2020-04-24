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

AAU, you can login, sign up, comment on a book, search for book.
