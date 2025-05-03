# Install icecream for logging/debugging
from icecream import ic
ic.configureOutput(prefix='[debug]')
ic.enable()

import flask
from views.root import home_app
from views.api_credential import cred_store

ic("Starting Flask app...")
app = flask.Flask(__name__)

# load external config file
app.config.from_pyfile('settings.py')

# register blueprint for the User interface
app.register_blueprint(home_app)

# register blueprint for the API for managing credential values
app.register_blueprint(cred_store, url_prefix='/api/credential')
