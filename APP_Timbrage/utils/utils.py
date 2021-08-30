from flask import session, redirect, url_for, flash, abort
from functools import wraps
"""
Check pour savoir si l'utilisateur c'est conncecté
"""
def si_user_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "loggedin" in session:
            return f(*args, **kwargs)
        else:
            flash("Veuillez-vous connecté ! ", "danger")
            return redirect(url_for('login'))
    return wrap
# decorator that check if a user is admin
def is_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['FK_role'] == 4:
            return f(*args, **kwargs)
        if session['FK_role'] == 5:
            return f(*args, **kwargs)
        else:
            abort(404)
    return wrap