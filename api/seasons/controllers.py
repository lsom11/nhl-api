from flask import Blueprint, jsonify, request, make_response

import json
import requests
from requests import HTTPError

seasons_blueprint = Blueprint('seasons', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/seasons'


@seasons_blueprint.route('/', methods=['GET'])
def get_seasons():
    try:
        r = requests.get(url=URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'seasons': res,
            'status_code': r.status_code
        }


@seasons_blueprint.route('/<season_id>', methods=['GET'])
def get_season(season_id):
    try:
        r = requests.get(url=URL + '/' + season_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'season': res,
            'status_code': r.status_code
        }

@seasons_blueprint.route('/current', methods=['GET'])
def get_current_season():
    try:
        r = requests.get(url=URL + '/current')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'season': res,
            'status_code': r.status_code
        }
