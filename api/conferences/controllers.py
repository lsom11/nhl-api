from flask import Blueprint, jsonify, request, make_response

import json
import requests
from requests import HTTPError

conferences_blueprint = Blueprint('conferences', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/conferences'


@conferences_blueprint.route('/', methods=['GET'])
def get_conferences():
    try:
        r = requests.get(url=URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'conferences': res['conferences'],
            'status_code': r.status_code
        }


@conferences_blueprint.route('/<conference_id>', methods=['GET'])
def get_team(conference_id):
    try:
        r = requests.get(url=URL + '/' + conference_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'team': res['conferences'][0],
            'status_code': r.status_code
        }
