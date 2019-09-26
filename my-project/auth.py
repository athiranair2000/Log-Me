from flask import Blueprint,render_template,redirect,url_for,request
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from . import db

auth=Blueprint('auth',__name__)
@auth.route('/login',methods=['POST'])
def login_post():
    email=request.form.get('email')
    password=request.form.get('password')
    remember=True if request.form.get('remember') else False
    
    # check if user actually exists
    user=User.query.filter_by(email=email).first()
    #check password by hashing it and comparing it to hashed password in database.
    if not user or not check_password_hash(user.password,password):
	flash('Please check your login details and try again.')
	return redirect(url_for('auth.login'))
	# if user doesn't exist or password is wrong,reloading the page.
	# if right credentials,
	return redirect(url_for('main.profile'))

@auth.route('/signup',methods=['POST'])
def signup_post():
    email=request.form.get('email')
    name=request.form.get('name')
    password=request.form.get('password')
    
    user=User.query.filter_by(email=email).first() # if presents in database
	
	if user: # redirect back to signup page.
		flash('Email address already exists')
		return redirect(url_for('auth.signup'))
	new_user=User(email=emal,name=name,password=generate_password_hash(password,method='sha256'))
	#to add new user
	db.session.add(new_user)
	db.session.commit()

	return redirect(url_for('auth.login'))
