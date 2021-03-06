#!flask/bin/python
import os

from flask import jsonify, abort, make_response, request, url_for, render_template, flash, redirect
from flask import request
from sqlalchemy import update

import json

from pprint import pprint

# package stuff
from flask_api.forms import *
#from flask_api.models import users
from flask_api import app, db, mail, mail_config

from flask_emails import Message

import requests
from time import time as gettime

from flask_emails import EmailsConfig

token = os.getenv("TOKEN")
head = {
    'Authorization': f'Token token="{token}"'
}

#EMAIL_COOLDOWN = 10*60 # 10 minutes

####################
#   Error Pages    #
####################
	
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(401)
def unauthorised_access(error):
    # 401 makes a login popup, 403 doesn't
    return make_response(jsonify({'error': 'Unauthorised access'}), 401)

###################
# GET
def getLastPrice():
  ticker_url = f'https://api.exchange.coinjar.com/products/XRPAUD/ticker'
  req = requests.get(ticker_url, headers=head)
  ticker = req.json()
  return float(ticker['last'])

####################
#      Routes      #
####################

# index
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html', title='Home')

# check
@app.route('/check', methods=['GET'])
def check():
    last = getLastPrice()
    email_pass = request.args.get('pass')
    if email_pass:
        config_copy = mail_config
        config_copy['EMAIL_HOST_PASSWORD'] = email_pass
        mail = EmailsConfig(config=config_copy)

        message = Message(config=mail, html=f'<html><p>{last}</p></html>',
                        subject=f"Daily Update - ${last}",
                        mail_from=("Cron Job", "testsmtpwagtail@gmail.com"))

        try:
            r = message.send(to=("Nick Jordan", "nickjordan289@gmail.com"))
        except Exception as e:
            print("Invalid mail settings")
    return jsonify({'last':last})

@app.route('/check_2', methods=['GET'])
def check2():
    last = getLastPrice()
    email_pass = request.args.get('pass')
    LIM = float(request.args.get('lim'))
    if email_pass:
        config_copy = mail_config
        config_copy['EMAIL_HOST_PASSWORD'] = email_pass
        mail = EmailsConfig(config=config_copy)

        message = Message(config=mail, html=f'<html><p>{last}</p></html>',
                        subject=f"Price Warning - ${last}",
                        mail_from=("Cron Job", "testsmtpwagtail@gmail.com"))

        if(last >= LIM):
            try:
                r = message.send(to=("Nick Jordan", "nickjordan289@gmail.com"))
            except Exception as e:
                print("Invalid mail settings")
    return jsonify({'last':last})
