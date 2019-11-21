from flask_api import app, db
#from flask_api.models import users

db.create_all() # makes sure all tables exist

if __name__ == '__main__':
    # use port=80 to remove port requirement in url
	app.run(port=80, debug=False) # 5000 is default for flask
