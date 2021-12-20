from flask import Flask, render_template, request
from sqlalchemy import Table, MetaData
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first_game.sqlite'
db = SQLAlchemy(app)

class example(db.Model):
	steam_appid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	apptype = db.Column(db.String)

def __init__(self, steam_appid, name, apptype):
	self.steam_appid = steam_appid	
	self.name = name
	self.apptype = apptype

def __repr__(self):
	return self.steam_appid, self.name, self.apptype	


@app.route('/', methods = ['GET'])
def index():
	games = example.query.all()
	for game in games:
		print(game.apptype)
		print(game.name)
	return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(debug = True)