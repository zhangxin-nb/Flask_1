import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import sessions
from flask import url_for
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['usernme']
        password = request.form['password']
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = 'Password is required'
        flash(error)
