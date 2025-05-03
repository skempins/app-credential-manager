import os

# Configure icecream for logging/debugging
from icecream import ic
app_debug = str(os.environ.get("APP_DEBUG"))
if app_debug.upper() == "TRUE":
    # Check if a debug prefix was defined
    debug_prefix = os.environ.get("APP_DEBUG_PREFIX")
    if debug_prefix == None:
        # no debug prefix defined, so set a default
        debug_prefix = "[debug]"

    print(f"Enabling APP_DEBUG mode with message prefix:", debug_prefix)
    ic.configureOutput(prefix=debug_prefix)
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
