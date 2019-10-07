from flask import Flask, url_for
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from teams.controllers import teams_blueprint as teams
from divisions.controllers import divisions_blueprint as divisions
from conferences.controllers import conferences_blueprint as conferences
from players.controllers import players_blueprint as players
from games.controllers import games_blueprint as games
from schedule.controllers import schedule_blueprint as schedule
from seasons.controllers import seasons_blueprint as seasons
from standings.controllers import standings_blueprint as standings
from stats.controllers import stats_blueprint as stats

from config import BaseConfig
from config import configure_app

import os.path

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/api/v1/docs'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Nhl Api"
    }
)

cors = CORS(app, resources={
    r'/api/v1/*': {
        'origins': BaseConfig.ORIGINS
    }
})

configure_app(app)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(teams, url_prefix='/api/v1/teams')
app.register_blueprint(divisions, url_prefix='/api/v1/divisions')
app.register_blueprint(conferences, url_prefix='/api/v1/conferences')
app.register_blueprint(players, url_prefix='/api/v1/players')
app.register_blueprint(games, url_prefix='/api/v1/games')
app.register_blueprint(schedule, url_prefix='/api/v1/schedule')
app.register_blueprint(seasons, url_prefix='/api/v1/seasons')
app.register_blueprint(standings, url_prefix='/api/v1/standings')
app.register_blueprint(stats, url_prefix='/api/v1/stats')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
