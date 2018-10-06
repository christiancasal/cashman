import mlbgame
import jsonpickle

from flask import Flask, jsonify, redirect
from flask_cors import CORS
from datetime import date
from documents.game import Game as GameDocument

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
	return redirect("/today")

@app.route("/today")
def todays_games():
	today = date.today()
	payload = []
 
	data = mlbgame.games(2018, 7, 4)
	games = mlbgame.combine_games(data)

	for game in games:
		data_obj = {}
		overview_data = overview(game.game_id)
		team_stats_data = team_stats(game.game_id)

		data_obj.update(overview_data)
		data_obj.update(team_stats_data)
		payload.append(data_obj)
	
		foo = GameDocument(
			game_id = data_obj.get('game_id'),
			away_team_id = data_obj.get('away_team_id'),
			home_team_id = data_obj.get('home_team_id'),
			home_code = data_obj.get('home_code'),
			away_code = data_obj.get('away_code'),
			home_pitching = jsonpickle.encode(data_obj.get('home_pitching')),
			away_pitching = jsonpickle.encode(data_obj.get('away_pitching')),
			home_additional_pitching = jsonpickle.encode(data_obj.get('home_additional_pitching')),
			away_additional_pitching = jsonpickle.encode(data_obj.get('away_additional_pitching')),
			home_batting = jsonpickle.encode(data_obj.get('home_batting')),
			away_batting = jsonpickle.encode(data_obj.get('away_batting')),
			home_additional_batting = jsonpickle.encode(data_obj.get('home_additional_batting')),
			away_additional_batting = jsonpickle.encode(data_obj.get('away_additional_batting'))
		)
		foo.save()

	dictionary = {
		"payload": payload
	}
	return jsonpickle.encode(dictionary)

def overview(id):
	data = mlbgame.overview(id)
	
	params = {
		'game_id': id,
		'away_team_id': data.away_team_id,
		'home_team_id': data.home_team_id,
		'home_code': data.home_code,
		'away_code': data.away_code
	}

	return params

def team_stats(id):
	data = mlbgame.team_stats(id)
	params = {
		'home_pitching': data.home_pitching,
		'away_pitching': data.away_pitching,
		'home_additional_pitching': data.home_additional_pitching,
		'away_additional_pitching': data.away_additional_pitching,
		'home_batting': data.home_batting,
		'away_batting': data.away_batting,
		'home_additional_batting': data.home_additional_batting,
		'away_additional_batting': data.away_additional_batting
	}

	return params

@app.route('/player')
def player():
	data = mlbgame.player_stats('2018_07_04_bosmlb_wasmlb_1')

	dictionary = {
		"payload": data
	}

	return jsonpickle.encode(dictionary)