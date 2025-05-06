CREATE TABLE credential
( credential_id TEXT PRIMARY KEY
, credential_nm TEXT
, credential_val TEXT)
;
CREATE UNIQUE INDEX credential_x1 ON credential (credential_nm)
;

CREATE TABLE client_app
( client_id TEXT PRIMARY KEY
, client_nm TEXT)
;
CREATE UNIQUE INDEX client_app_x1 ON client_app (client_nm)
;

CREATE TABLE client_credential
( client_id TEXT REFERENCES client_app (client_id)
, credential_id TEXT REFERENCES credential (credential_id) )
;
CREATE UNIQUE INDEX client_credential_x1 ON client_credential (client_id, credential_id)
;