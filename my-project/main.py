from flask import Blueprint,render_template
from . import db
from flask_login import login_required,current_user

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

@main.route('/profile')
@login_required  #to get details of only logged in people not any external user 

def profile():
	return render_template('profile.html',name=current_user.name)

