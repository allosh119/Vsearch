from flask import session
from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        if 'Logged_in' in session:
            return func(*args, **kargs)
        return 'Please Login First to view the page!'
    return wrapper
