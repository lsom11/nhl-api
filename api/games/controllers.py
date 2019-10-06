from flask import Blueprint, jsonify, request, make_response

import json
import requests
from requests import HTTPError

games_blueprint = Blueprint('games', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/game'
GAME_TYPES_URL = 'https://statsapi.web.nhl.com/api/v1/gameTypes'
PLAY_TYPES_URL = 'https://statsapi.web.nhl.com/api/v1/playTypes'


@games_blueprint.route('/gameTypes', methods=['GET'])
def get_game_types():
    try:
        r = requests.get(url=GAME_TYPES_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'gameTypes': res,
            'status_code': r.status_code
        }

@games_blueprint.route('/playTypes', methods=['GET'])
def get_play_types():
    try:
        r = requests.get(url=PLAY_TYPES_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'playTypes': res,
            'status_code': r.status_code
        }


@games_blueprint.route('/<game_id>/livescore', methods=['GET'])
def get_livescore(game_id):
    try:
        r = requests.get(url=URL + '/' + game_id + '/feed/live')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'gameData': res['gameData'],
            'status_code': r.status_code
        }

@games_blueprint.route('/<game_id>/boxscore', methods=['GET'])
def get_boxscore(game_id):
    try:
        r = requests.get(url=URL + '/' + game_id + '/boxscore')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'gameData': res['teams'],
            'status_code': r.status_code
        }

@games_blueprint.route('/<game_id>/linescore', methods=['GET'])
def get_linescore(game_id):
    try:
        r = requests.get(url=URL + '/' + game_id + '/linescore')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'gameData': res,
            'status_code': r.status_code
        }

@games_blueprint.route('/<game_id>/content', methods=['GET'])
def get_content(game_id):
    try:
        r = requests.get(url=URL + '/' + game_id + '/content')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'content': res['editorial'],
            'status_code': r.status_code
        }
