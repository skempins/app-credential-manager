import os
import uuid
import sqlite3
from icecream import ic

class CredentialStore:
    """A class to manage credentials in a secure store."""
    db_file = 'database.db'
    create_schema = 'app/create_schema.sql'

    ########################
    """Initialize the database."""
    def __init__(self):

        print("Checking for database file: ", self.db_file)
        if self.check_db():
            print("Database exists.")
        else:
            print("Database does not exist, creating.")
            ic("Opening schema definition file...")
            ic(self.create_schema)
            try:
                with open(self.create_schema, 'r') as rf:
                    # Read the schema from the file
                    sqlscript = rf.read()
            except:
                ic("Schema definition file not found.")
                exit(0)

            ic("Opening database connection...")
            try:
                with sqlite3.connect(self.db_file) as conn:
                    ic("Creating schema...")
                    conn.executescript(sqlscript)
                print("Schema created.")
            except sqlite3.Error as e:
                print(f'Error: {e}')
                exit(0)

    ########################
    def check_db(self):
        ic("Checking for database file...")
        ic(self.db_file)
        return os.path.exists(self.db_file)

    ########################
    """Add a new credential to the store."""
    def add_credential(self, name, value):
        sql_stmt = "INSERT INTO credential (credential_id, credential_nm, credential_val) VALUES (?,?,?)"

        ic("Inserting credential...")
        id = str(uuid.uuid4())
        ic(name, id)
        try:
            with sqlite3.connect(self.db_file) as conn:
                ic(sql_stmt)
                conn.execute(sql_stmt, [id, name, value])
                conn.commit()
            return {"ID": id}
        except sqlite3.Error as e:
            return {"Error": str(e)}
        
    ########################
    """Retrieve a credential from the store."""
    def get_credential(self, name):
        sql_stmt = "SELECT credential_id, credential_val FROM credential WHERE credential_nm = ?"

        ic("Getting credential for...")
        ic(name)
        return_value = {}
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_stmt, [name])
                for row in cursor.fetchall():
                    ic(row)
                    return_value['Name'] = name
                    return_value['ID'] = row[0]
                    return_value['Value'] = row[1]
            return return_value
        except sqlite3.Error as e:
            return {"Error": str(e)}

    ########################
    """Remove a credential from the store."""
    def delete_credential(self, name):
        sql_stmt = "DELETE FROM credential WHERE credential_nm = ?"

        ic("Deleting credential...")
        ic(name)
        try:
            with sqlite3.connect(self.db_file) as conn:
                conn.execute(sql_stmt, [name])
            return True
        except sqlite3.Error as e:
            return {"Error": str(e)}

    ########################
    def export_all(self):
        sql_stmt = "SELECT credential_id, credential_nm, credential_val FROM credential"

        ic("Exporting all credentials...")
        print("ID, Name, Value")
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_stmt)
                for row in cursor.fetchall():
                    id, name, value = row
                    print(f'{id}; {name}; {value}')
            return True
        except sqlite3.Error as e:
            return {"Error": str(e)}

    ########################
    # Add a new client to the store.
    def add_client(self, name):
        sql_stmt = "INSERT INTO client_app (client_id, client_nm) VALUES (?,?)"

        ic("Inserting client...")
        id = str(uuid.uuid4())
        ic(name, id)
        try:
            with sqlite3.connect(self.db_file) as conn:
                ic(sql_stmt)
                conn.execute(sql_stmt, [id, name])
                conn.commit()
            return {"ID": id}
        except sqlite3.Error as e:
            return {"Error": str(e)}

    ########################
    # Add a client to a credential
    def add_client_credential(self, client_id, credential_id):
        sql_stmt = "INSERT INTO client_credential (client_id, credential_id) VALUES (?,?)"

        ic("Mapping client to credential...")
        ic(client_id, credential_id)
        try:
            with sqlite3.connect(self.db_file) as conn:
                ic(sql_stmt)
                conn.execute(sql_stmt, [client_id, credential_id])
                conn.commit()
            return True
        except sqlite3.Error as e:
            return {"Error": str(e)}

    ########################
    # Map a client to a credential
    def map_client_credential(self, client_nm, credential_nm):
        sql_get_client = "SELECT client_id FROM client_app WHERE client_nm = ?"
        sql_get_credential = "SELECT credential_id FROM credential WHERE credential_nm = ?"

        ic("Mapping client to credential...")
        ic(client_nm, credential_nm)
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_get_client, [client_nm])
                row = cursor.fetchone()
                if row is None:
                    ic("Client not found")
                    return {"Error": "Client not found"}
                client_id = row[0]
                ic(client_id)

                cursor.execute(sql_get_credential, [credential_nm])
                row = cursor.fetchone()
                if row is None:
                    return {"Error": "Credential not found"}
                credential_id = row[0]
                ic(credential_id)
 
            return self.add_client_credential(client_id, credential_id)
        except sqlite3.Error as e:
            return {"Error": str(e)}

    ########################
    # Get all credentials for a client
    def get_client_credentials(self, client_nm):
        sql_stmt = """SELECT credential_nm 
            FROM client_credential 
            INNER JOIN credential ON client_credential.credential_id = credential.credential_id 
            INNER JOIN client_app ON client_credential.client_id = client_app.client_id 
            WHERE client_app.client_nm = ?
            ORDER BY credential_nm
            """

        ic("Getting credentials for client...")
        ic(client_nm)
        return_value = []
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_stmt, [client_nm])
                for row in cursor.fetchall():
                    return_value.append(row[0])
            return return_value
        except sqlite3.Error as e:
            return {"Error": str(e)}