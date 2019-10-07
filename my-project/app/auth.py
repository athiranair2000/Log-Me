from flask import Blueprint
from . import db
from flask_login import login_user
from .models import User


auth=Blueprint('auth',__name__)
@auth.route('/login',methods=['POST'])
def login_post():
    login_user(user,remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return 'Signup'

