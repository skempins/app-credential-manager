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

# register blueprints
app.register_blueprint(home_app)
app.register_blueprint(cred_store, url_prefix='/api/credential')

#ic(mycredential_store.get_credential("app1"))  # Output: user123
#ic(mycredential_store.get_credential("auth_token"))  # Output: abc123
