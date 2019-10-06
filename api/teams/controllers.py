from flask import Blueprint, jsonify, request, make_response

import json
import requests
from requests import HTTPError

teams_blueprint = Blueprint('teams', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/teams'
VENUES_URL = ' https://statsapi.web.nhl.com/api/v1/venues'


@teams_blueprint.route('/', methods=['GET'])
def get_teams():
    try:
        r = requests.get(url=URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'teams': res['teams'],
            'status_code': r.status_code
        }

@teams_blueprint.route('/stadiums', methods=['GET'])
def get_stadiums():
    try:
        r = requests.get(url=VENUES_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'stadiums': res['venues'],
            'status_code': r.status_code
        }

@teams_blueprint.route('/stadiums/<stadium_id>', methods=['GET'])
def get_stadium(stadium_id):
    try:
        r = requests.get(url=VENUES_URL + '/' + stadium_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'stadium': res['venues'][0],
            'status_code': r.status_code
        }


@teams_blueprint.route('/<team_id>', methods=['GET'])
def get_team(team_id):
    try:
        r = requests.get(url=URL + '/' + team_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'team': res['teams'][0],
            'status_code': r.status_code
        }
