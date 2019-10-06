from flask import Blueprint, jsonify, request, make_response

import json
import requests
from requests import HTTPError

divisions_blueprint = Blueprint('divisions', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/divisions'


@divisions_blueprint.route('/', methods=['GET'])
def get_divisions():
    try:
        r = requests.get(url=URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'divisions': res['divisions'],
            'status_code': r.status_code
        }


@divisions_blueprint.route('/<division_id>', methods=['GET'])
def get_division(division_id):
    try:
        r = requests.get(url=URL + '/' + division_id)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'division': res['division'][0],
            'status_code': r.status_code
        }
