import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))


def loadbooks():
    with open("books.csv", "r") as f:
        reader = csv.reader(f)
        for isbn, title, author, year in reader:
            engine.execute(
                "INSERT INTO books(isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {"isbn": isbn, "title": title, "author": author, "year": year}
            )
        engine.commit()
