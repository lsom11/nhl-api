from flask import Flask, url_for
from flask_cors import CORS

from teams.controllers import teams_blueprint as teams
from divisions.controllers import divisions_blueprint as divisions
from conferences.controllers import conferences_blueprint as conferences

from config import BaseConfig
from config import configure_app

import os.path

app = Flask(__name__)

cors = CORS(app, resources={
    r'/api/v1/*': {
        'origins': BaseConfig.ORIGINS
    }
})

configure_app(app)

app.register_blueprint(teams, url_prefix='/api/v1/teams')
app.register_blueprint(divisions, url_prefix='/api/v1/divisions')
app.register_blueprint(conferences, url_prefix='/api/v1/conferences')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
