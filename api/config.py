import os

class BaseConfig(object):
    """ Base config class. This fields will use by production and development server """

    ORIGINS = ["*"]  # for api calls
    SECRET_KEY = 'YOUR SECRET KEY'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}



class Development(BaseConfig):
    """ Development config. We use Debug mode """

    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'


# Currently we only have development config.
# If you have production, you will need to pass it to here.
config = {
    'development': 'config.Development'
}


def configure_app(app):
    """ 
        App configuration will be here. 

        Parameters
        ----------

        app : Flask
            app instance
    """

    app.config.from_object(config['development'])
