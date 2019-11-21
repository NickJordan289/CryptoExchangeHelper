#!flask/bin/python
from flask import jsonify, abort, make_response, request, url_for, render_template, flash, redirect
from flask import request
from sqlalchemy import update

import json

from pprint import pprint

# package stuff
from flask_api.forms import *
#from flask_api.models import users
from flask_api import app, db

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

####################
#      Routes      #
####################

# index
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html', title='Home')

# All Tasks
@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({})