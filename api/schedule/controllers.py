from flask import Blueprint, jsonify, request, make_response

import json
import requests
from requests import HTTPError

schedule_blueprint = Blueprint('schedule', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/schedule'


@schedule_blueprint.route('/todays_schedule', methods=['GET'])
def get_todays_schedule():
    try:
        r = requests.get(url=URL)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        res = json.loads(r.content)
        return {
            'schedule': res,
            'status_code': r.status_code
        }
