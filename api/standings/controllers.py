from flask import Blueprint, jsonify, request, make_response
from utils import url_query_builder

import json
import requests
from requests import HTTPError

standings_blueprint = Blueprint('standings', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/standings'
STANDINGS_TYPES_URL = 'https://statsapi.web.nhl.com/api/v1/standingsTypes'


@standings_blueprint.route('/', methods=['GET'])
def get_standings():
    try:
        args = request.args.to_dict()
        query = url_query_builder(args)
        r = requests.get(url=URL + query)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'standings': res,
            'status_code': r.status_code
        }

@standings_blueprint.route('/types', methods=['GET'])
def get_standings_types():
    try:
        r = requests.get(url=STANDINGS_TYPES_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'types': res,
            'status_code': r.status_code
        }


@standings_blueprint.route('/current', methods=['GET'])
def get_current_standings():
    try:
        args = request.args.to_dict()
        query = url_query_builder(args)
        r = requests.get(url=URL + query)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'standings': res,
            'status_code': r.status_code
        }

@standings_blueprint.route('/season/<season_id>', methods=['GET'])
def get_season_standings(season_id):
    try:
        args = request.args.to_dict()
        query = url_query_builder(args)
        r = requests.get(url=URL + query)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'standings': res,
            'status_code': r.status_code
        }