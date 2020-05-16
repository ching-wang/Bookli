import requests
import os

API_KEY = os.environ["GOODREADS_API_KEY"]


def get_reviews(isbn: str):
    res = requests.get(
        "https://www.goodreads.com/book/review_counts.json",
        params={'key': API_KEY, 'isbns': isbn})
    json = res.json()
    return json["books"][0]
