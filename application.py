import requests
import os
import csv

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route("/books")
def books():
    allbooks = db.execute(
        "SELECT isbn, title, author, year FROM books").fetchall()
    return render_template('books.html', books=allbooks)


# @app.route("/user/:")
# def user():
#     user = db.execute(
#         "SELECT user FROM users WHERE id ==== "
#     )

if __name__ == "__main__":
    main()
