'''
This implements the API for managing credential values
'''
from icecream import ic
import flask
import markupsafe

# The credential_store manages the credentials
import credential_store
mycredential_store = credential_store.CredentialStore()

# define the blueprint for the API
cred_store = flask.Blueprint('cred_store', __name__)

########################
# Get Credential
@cred_store.route('/get/<credential>', methods=['GET'])
def get_credential(credential):
    return_value = mycredential_store.get_credential(credential)
    ic(return_value)
    if "ID" in return_value:
        return flask.jsonify({"Status": "Success", "Credential": return_value})
    else: 
        if "Error" in return_value:
            return flask.jsonify({"Status": "Failure", "Message": return_value})
        else:
            return flask.jsonify({"Status": "Success", "Message": "Credential does not exist"})

########################
# Add Credential
@cred_store.route('/add', methods=['POST'])
def add_credential():
    if 'name' in flask.request.form:
        if 'value' in flask.request.form:
            return_value = mycredential_store.add_credential(flask.request.form['name'], flask.request.form['value'])
            ic(return_value)
            if "ID" in return_value:
                return flask.jsonify({"Status": "Success", "Credential": return_value})
            else:
                return flask.jsonify({"Status": "Failure", "Message": return_value})
        else:
            return flask.jsonify({"Status": "Failure", "Message": "missing credential value"})
    else:
        return flask.jsonify({"Status": "Failure", "Message": "missing credential name"})

########################
# Delete Credential
@cred_store.route('/delete/<credential>', methods=['GET'])
def delete_credential(credential):
    return_value = mycredential_store.delete_credential(credential)
    ic(return_value)
    if type(return_value) == type(True):
        return flask.jsonify({"Status": "Success"})
    else:
        return flask.jsonify({"Status": "Failure", "Message": return_value})

########################
# Export all credential values
@cred_store.route('/exportall', methods={'GET'})
def export_all():
    return_value = mycredential_store.export_all()
    ic(return_value)
    if type(return_value) == type(True):
        return flask.jsonify({"Status": "Success"})
    else:
        return flask.jsonify({"Status": "Failure", "Message": return_value})

########################
# Add a new client to the store.
@cred_store.route('/addclient', methods=['POST'])
def add_client():
    if 'name' in flask.request.form:
        return_value = mycredential_store.add_client(flask.request.form['name'])
        ic(return_value)
        if "ID" in return_value:
            return flask.jsonify({"Status": "Success", "Credential": return_value})
        else:
            return flask.jsonify({"Status": "Failure", "Message": return_value})
    else:
        return flask.jsonify({"Status": "Failure", "Message": "missing client name"})

########################
# Map a client to a credential
@cred_store.route('/mapclientcredential', methods=['POST'])
def map_client_credential():
    if 'client_name' in flask.request.form:
        if 'credential_name' in flask.request.form:
            return_value = mycredential_store.map_client_credential(flask.request.form['client_name'], flask.request.form['credential_name'])
            ic(return_value)
            if type(return_value) == type(True):
                return flask.jsonify({"Status": "Success"})
            else:
                return flask.jsonify({"Status": "Failure", "Message": return_value})
        else:
            return flask.jsonify({"Status": "Failure", "Message": "missing credential name"})
    else:
        return flask.jsonify({"Status": "Failure", "Message": "missing client name"})

########################
# get Client credentials
@cred_store.route('/getclientcredentials/<client>', methods=['GET'])
def get_client_credentials(client):
    return_value = mycredential_store.get_client_credentials(client)
    ic(return_value)
    if "Error" in return_value:
        return flask.jsonify({"Status": "Failure", "Message": return_value})
    else:
        return flask.jsonify({"Status": "Success", "Credential": return_value})
