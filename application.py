from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from helper import *
from flask_session import Session
from flask import Flask, request, session, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap

import requests
import os
import csv
import hashlib
import random
import string
import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO)

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
    books = db.execute(
        "SELECT isbn, title, author, year FROM books").fetchmany(100)
    return render_template('home.html', books=books)


@app.route('/sign-up', methods=["get"])
def get_sign_up():
    return render_template('sign_up.html')


@app.route('/post-sign-up', methods=["post"])
def post_sign_up():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    # Check for existing user with this username or email.
    existing = db.execute(
        "SELECT * FROM users WHERE username = :username OR email = :email",
        {"username": username, "email": email}).fetchone()
    if existing:
        return render_template('sign_up.html', message="Username or email already taken")

    # Hash the password with a salt for secure storage.
    salt = make_salt()
    hashed_password = hash_password(password, salt)
    password_hash_with_salt = f"{salt}:{hashed_password}"

    # Insert the new user into the DB.
    logging.info("Inserting new user")
    db.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (:username, :email, :password_hash) RETURNING id",
        {
            "username": username,
            "email": email,
            "password_hash": password_hash_with_salt
        })
    db.commit()

    user_data = db.execute(
        "SELECT * FROM users WHERE username = :username",
        {"username": username}).fetchone()

    logging.info("Insert new user data: {}", user_data)

    # Log the new user in.
    session["user_data"] = user_data

    return redirect(url_for("profile"))


@app.route("/login", methods=["get"])
def get_login():
    return render_template("login.html")


@app.route("/post-login", methods=["post"])
def post_login():
    username = request.form.get("username")

    user_data = db.execute(
        "SELECT * FROM users WHERE username = :username",
        {'username': username}).fetchone()

    if not user_data:
        # User not found: send back to login form.
        return render_template("login.html", message="User not found")

    submitted_password = request.form.get("password")

    # Password hash is stored in the DB like this: "salt:hash"
    stored_password = str(user_data["password_hash"]).split(":")
    stored_salt = stored_password[0]
    stored_hash = stored_password[1]

    # Make a salted hash of the submitted password.
    submitted_password_hash = hash_password(submitted_password, stored_salt)

    if stored_hash != submitted_password_hash:
        # Wrong password: send back to login.
        return render_template("login.html", message="Wrong password")

    # Log the user in in Flask by setting the user data in session.
    session["user_data"] = user_data

    return redirect(url_for("profile"))


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    return redirect(url_for("home"))


@app.route("/profile")
def profile():
    # if session.length < 0:
    #     return render_template("login.html", message="you must log in to view this page")
    return render_template('profile.html')


@app.route("/books")
def books():
    allbooks = db.execute(
        "SELECT isbn, title, author, year FROM books").fetchall()
    return render_template('books.html', books=allbooks)


@app.route("/book")
def book():
    return render_template("book.html")


def make_salt() -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(16))


def hash_password(password: str, salt: str) -> str:
    m = hashlib.sha256()
    m.update(f"{password}{salt}".encode("utf-8"))
    return m.hexdigest()


if __name__ == "__main__":
    main()
