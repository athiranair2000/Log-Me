from flask import flask

# Initialise the app

app=Flask(__name__,instance_relative_config=True)

# Load the views

From app import views

app.config.from_object('config')

