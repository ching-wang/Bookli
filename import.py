import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

with open("books.csv", "r") as f:
    reader = csv.DictReader(f)
    row_num = 0
    for row in reader:
        row_num = row_num + 1
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                   {"isbn": str(row["isbn"]),
                    "title": str(row["title"]),
                    "author": str(row["author"]),
                    "year": int(row["year"])})
        print(f"row {row_num}")
    db.commit()
