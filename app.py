from flask import Flask, render_template, request
from sqlalchemy import Table, MetaData, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
import app
import os
import socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steam_games.db'
db = SQLAlchemy(app)

class games(db.Model):
	steam_appid = Column(Integer, primary_key=True)
	game_type = Column(String)
	game_name = Column(String)
	required_age = Column(Integer)
	is_free  = Column(String)
	detailed_description = Column(String)
	about_the_game = Column(String)
	short_description = Column(String)
	header_image = Column(String)
	website = Column(String)
	pc_requirements_min = Column(String)
	pc_requirements_recomm = Column(String)
	mac_requirements_min = Column(String)
	mac_requirements_recomm = Column(String)
	price_currency = Column(String)
	price_initial = Column(Integer)
	price_final = Column(Integer)
	price_discount_percent = Column(Integer)
	price_initial_formatted = Column(String)
	price_final_formatted = Column(String)
	release_date_coming_soon = Column(String)
	release_date = Column(String)
	support_info_url = Column(String)
	support_info_email = Column(String)
	support_info_background = Column(String)
	num_reviews = Column(Integer)
	review_score = Column(Integer)
	total_positive = Column(Integer)
	total_negative = Column(Integer)
	total_reviews = Column(Integer)
	platforms_windows = Column(String)
	platforms_mac = Column(String)
	platforms_linux = Column(String)	

def __init__(self, steam_appid, game_type, game_name, required_age, is_free, detailed_description, about_the_game, short_description, header_image, website, pc_requirements_min, pc_requirements_recomm, mac_requirements_min, mac_requirements_recomm, price_currency, price_initial, price_final, price_discount_percent, price_initial_formatted, price_final_formatted, release_date_coming_soon, release_date, support_info_url, support_info_background, num_reviews, review_score, total_positive, total_negative, total_reviews, platforms_windows, platforms_mac, platforms_linux):
	self.steam_appid = steam_appid	
	self.game_name = game_name
	self.game_type = game_type
	self.required_age = required_age
	self.is_free = is_free
	self.detailed_description = detailed_description
	self.about_the_game = about_the_game
	self.short_description = short_description
	self.header_image = header_image
	self.website = website
	self.pc_requirements_min = pc_requirements_recomm
	self.pc_requirements_recomm = pc_requirements_recomm
	self.mac_requirements_min = mac_requirements_min
	self.mac_requirements_recomm = mac_requirements_recomm
	self.price_currency = price_currency
	self.price_initial = price_initial
	self.price_final = price_final
	self.price_discount_percent = price_discount_percent
	self.price_initial_formatted = price_initial_formatted
	self.price_final_formatted = price_final_formatted
	self.release_date_coming_soon = release_date_coming_soon
	self.release_date = release_date
	self.support_info_url = support_info_url
	self.support_info_email = support_info_email
	self.support_info_background = support_info_background
	self.num_reviews = num_reviews
	self.review_score = review_score
	self.total_positive = total_positive
	self.total_negative = total_negative
	slf.total_reviews = total_reviews
	self.platforms_windows = platforms_windows
	self.platforms_mac = platforms_mac
	self.platforms_linux = platforms_linux

def __repr__(self):
	return self.steam_appid, self.game_name, self.game_type,  self.required_age, self.is_free, self.detailed_description, self.about_the_game, self.short_description, self.header_image, self.website, self.pc_requirements_min, self.pc_requirements_recomm, self.mac_requirements_min, self.mac_requirements_recomm, self.price_currency, self.price_initial, self.price_final, self.price_discount_percent, self.price_initial_formatted, self.price_final_formatted, self.release_date_coming_soon, self.release_date, self.support_info_url, self.support_info_background, self.num_reviews, self.review_score, self.total_positive, self.total_negative, self.total_reviews, self.platforms_windows, self.platforms_mac, self.platforms_linux	


@app.route('/', methods = ['GET'])
def index():
	game = games.query.all()
	return render_template('index.html', game=game)

if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    app.run(host=local_ip, port=os.environ.get('PORT'), debug=True)