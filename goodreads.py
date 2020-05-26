import requests
import os
import logging

API_KEY = os.environ["GOODREADS_API_KEY"]


def get_reviews(isbn: str):
    try:
        res = requests.get(
            "https://www.goodreads.com/book/review_counts.json",
            params={'key': API_KEY, 'isbns': isbn})
        json = res.json()
        return json["books"][0]
    except Exception as e:
        logging.error(e)
        return {}
