import os
from dotenv import load_dotenv, find_dotenv

from flask import Flask
#from flaskext.mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_emails import EmailsConfig

load_dotenv(find_dotenv(), verbose=True)

# init app and config
app = Flask(__name__)
app.config['SECRET_KEY'] = '60339867c2c323b1f9afefbc297129c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) 

#mail_config = {'EMAIL_HOST': 'smtp.gmail.com', 
#                'EMAIL_PORT': 587, 
#                'EMAIL_HOST_USER':'testsmtpwagtail@gmail.com',
#                'EMAIL_HOST_PASSWORD': os.getenv("EMAIL_PASS"),
#                'EMAIL_USE_TLS':True,
#                'EMAIL_TIMEOUT': 10}
mail_config = {'EMAIL_HOST': 'smtp.gmail.com', 
                'EMAIL_PORT': 587, 
                'EMAIL_HOST_USER':'testsmtpwagtail@gmail.com',
                'EMAIL_USE_TLS':True,
                'EMAIL_TIMEOUT': 10}

mail = EmailsConfig(config=mail_config)


# required at bottom in order to prevent circular dependancy, after everything has been intialised
from flask_api import views
