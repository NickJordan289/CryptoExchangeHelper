from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init app and config
app = Flask(__name__)
app.config['SECRET_KEY'] = '60339867c2c323b1f9afefbc297129c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) 

# required at bottom in order to prevent circular dependancy, after everything has been intialised
from flask_api import views
