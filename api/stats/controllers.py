from flask import Blueprint, jsonify, request, make_response

import json
import requests
from requests import HTTPError
from utils import url_query_builder

stats_blueprint = Blueprint('stats', __name__)

TEAM_STATS_URL = 'https://statsapi.web.nhl.com/api/v1/teams'
PLAYER_STATS_URL = 'https://statsapi.web.nhl.com/api/v1/people/'
AWARDS_URL = 'https://statsapi.web.nhl.com/api/v1/people/awards'
STATS_TYPES_URL = 'https://statsapi.web.nhl.com/api/v1/statTypes'


@stats_blueprint.route('/types', methods=['GET'])
def get_stat_types():
    try:
        r = requests.get(url=STATS_TYPES_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'statTypes': res,
            'status_code': r.status_code
        }

@stats_blueprint.route('/team/<team_id>', methods=['GET'])
def get_team_stats(team_id):
    try:
        r = requests.get(url=TEAM_STATS_URL + '/' + team_id + '/stats')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'stats': res['stats'],
            'status_code': r.status_code
        }

@stats_blueprint.route('/player/<player_id>', methods=['GET'])
def get_player_stats(player_id):
    try:
        args = request.args.to_dict()
        query = url_query_builder(args)
        r = requests.get(url=PLAYER_STATS_URL + '/' + player_id + '/stats' + query)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'stats': res,
            'status_code': r.status_code
        }

@stats_blueprint.route('/awards', methods=['GET'])
def get_awards():
    try:
        r = requests.get(url=AWARDS_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'awards': res,
            'status_code': r.status_code
        }

@stats_blueprint.route('/awards/<award_id>', methods=['GET'])
def get_award(award_id):
    try:
        r = requests.get(url=AWARDS_URL + '/' + award_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'award': res,
            'status_code': r.status_code
        }

