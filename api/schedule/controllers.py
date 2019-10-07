from flask import Blueprint, jsonify, request, make_response
from utils import url_query_builder

import json
import requests
from requests import HTTPError

schedule_blueprint = Blueprint('schedule', __name__)

URL = 'https://statsapi.web.nhl.com/api/v1/schedule'


@schedule_blueprint.route('/', methods=['GET'])
def get_schedule():
    try:
        args = request.args.to_dict()
        query = url_query_builder(args + query)
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
