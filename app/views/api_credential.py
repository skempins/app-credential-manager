from icecream import ic
import flask
import markupsafe
import credential_store

mycredential_store = credential_store.CredentialStore()

cred_store = flask.Blueprint('cred_store', __name__)

@cred_store.route('/get/<credential>', methods=['GET'])
def get_credential(credential):
    return_value = mycredential_store.get_credential(markupsafe.escape(credential))
    if return_value == None:
        return "None"
    else:
        return return_value

@cred_store.route('/add', methods=['GET','POST'])
def add_credential():
#    ic(flask.request.form['name'])
#    ic(flask.request.form['credential'])

    if 'name' in flask.request.form:
        if 'credential' in flask.request.form:
            mycredential_store.add_credential(flask.request.form['name'], flask.request.form['credential'])
            return flask.jsonify({"Status": "Success"})
        else:
            return flask.jsonify({"Reason": "missing credential value"})
    else:
        return flask.jsonify({"Reason": "missing name"})

