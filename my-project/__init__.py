from flask import flask__
from flask_sqlalchemy import flask_sqlalchemy

db=SQLAlchemy()
# initialising SQLALchemy to connect it with model

def create_app():
# Initialise the app
app=Flask(__name__,instance_relative_config=True)
app.config['SECRET_KEY']=''
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://db.sqlite'
db.init_app(app)

# blue print for auth routes in application
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

return app


# Load the views

From app import views

app.config.from_object('config')

