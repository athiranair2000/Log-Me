from flask import Flask
from flask_sqlalchemy import flask_SQLAlchemy
from flask import LoginManager 
from flask_migrate import Migrate
db=SQLAlchemy()
# initialising SQLALchemy to connect it with model

def create_app():
# Initialise the app
	app=Flask(__name__,instance_relative_config=True)
	db=SQLALchemy(app)
	migrate = Migrate(app,db)
	manager=Manager(app)
	db.init_app(app)
	login_manager=LoginManager()
	login_manager.login_view='auth.login'
	login_manager.init_app(app)

# blue print for auth routes in application
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)




# Load the views

from app import views

from app import routes,models


from .models import User
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))





if __name__=='__main__':
	manager.run()
