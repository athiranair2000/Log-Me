from flask import Blueprint
from . import db

main=Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@auth.route('/login')
def index():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('SignUp.html')

