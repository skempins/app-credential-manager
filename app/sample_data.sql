INSERT INTO credential (credential_id, credential_nm, credential_val) VALUES ('8146210b-a0ce-4a31-82ff-a38f6fa1c50f','test1','secret-value 1');
INSERT INTO credential (credential_id, credential_nm, credential_val) VALUES ('77f44e3d-1004-48e1-889f-5b6fe8908be2','test2','secret-value 2');
INSERT INTO credential (credential_id, credential_nm, credential_val) VALUES ('797bd425-65ed-41df-8710-22f48c9891a6','test3','secret-value 3');
INSERT INTO credential (credential_id, credential_nm, credential_val) VALUES ('9191bf16-e0cd-4989-b379-121ecf8ebfc0','test4','secret-value 4');

INSERT INTO client_app (client_id, client_nm) VALUES ('6c45f31b-d0db-4af2-b2af-855a540611dc','App1');
INSERT INTO client_app (client_id, client_nm) VALUES ('e8fc3634-0601-4124-8c13-0a851f9eecfb','App2');
INSERT INTO client_app (client_id, client_nm) VALUES ('ec354874-e96f-416d-be76-16dc48496479','App3');

INSERT INTO client_credential (client_id, credential_id) VALUES ('e8fc3634-0601-4124-8c13-0a851f9eecfb','77f44e3d-1004-48e1-889f-5b6fe8908be2');
INSERT INTO client_credential (client_id, credential_id) VALUES ('6c45f31b-d0db-4af2-b2af-855a540611dc','8146210b-a0ce-4a31-82ff-a38f6fa1c50f');
INSERT INTO client_credential (client_id, credential_id) VALUES ('6c45f31b-d0db-4af2-b2af-855a540611dc','77f44e3d-1004-48e1-889f-5b6fe8908be2');
INSERT INTO client_credential (client_id, credential_id) VALUES ('6c45f31b-d0db-4af2-b2af-855a540611dc','797bd425-65ed-41df-8710-22f48c9891a6');
INSERT INTO client_credential (client_id, credential_id) VALUES ('6c45f31b-d0db-4af2-b2af-855a540611dc','9191bf16-e0cd-4989-b379-121ecf8ebfc0');
INSERT INTO client_credential (client_id, credential_id) VALUES ('e8fc3634-0601-4124-8c13-0a851f9eecfb','8146210b-a0ce-4a31-82ff-a38f6fa1c50f');
INSERT INTO client_credential (client_id, credential_id) VALUES ('ec354874-e96f-416d-be76-16dc48496479','77f44e3d-1004-48e1-889f-5b6fe8908be2');
INSERT INTO client_credential (client_id, credential_id) VALUES ('ec354874-e96f-416d-be76-16dc48496479','797bd425-65ed-41df-8710-22f48c9891a6');
