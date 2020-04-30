from flask import redirect, session, flash
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get("username")is None:
            flash("You need to login first")
            return redirect("/login")
        else:
            return f(*args, **kwargs)
    return wrap
