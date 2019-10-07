from flask import Blueprint, jsonify, request, make_response
from utils import url_query_builder

import json
import requests
from requests import HTTPError

players_blueprint = Blueprint('players', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/people'
DRAFT_URL = 'https://statsapi.web.nhl.com/api/v1/draft'
PROSPECTS_URL = 'https://statsapi.web.nhl.com/api/v1/draft/prospects'


@players_blueprint.route('/draft', methods=['GET'])
def get_draft():
    try:
        r = requests.get(url=DRAFT_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'draft': res['drafs'],
            'status_code': r.status_code
        }

@players_blueprint.route('/draft/<draft_id>', methods=['GET'])
def get_draft_by_year(draft_id):
    try:
        r = requests.get(url=DRAFT_URL + '/' + draft_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'draft': res['drafts'][0],
            'status_code': r.status_code
        }

@players_blueprint.route('/prospects', methods=['GET'])
def get_prospects():
    try:
        r = requests.get(url=PROSPECTS_URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'players': res,
            'status_code': r.status_code
        }


@players_blueprint.route('/<player_id>', methods=['GET'])
def get_player(player_id):
    try:
        args = request.args.to_dict()
        query = url_query_builder(args)
        r = requests.get(url=URL + '/' + player_id + query)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'player': res['players'][0],
            'status_code': r.status_code
        }

@players_blueprint.route('/prospects/<player_id>', methods=['GET'])
def get_prospect(player_id):
    try:
        r = requests.get(url=PROSPECTS_URL + '/' + player_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'prospect': res,
            'status_code': r.status_code
        }
