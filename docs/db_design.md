# Database Design

Credential
----------
- CredentialID: PK
- Name
- Credential

ClientApp
------------------
- ClientID: PK
- Name

Client/Credential Access
------------------------
- ClientID: FK -> ClientApp
- CredentialID: FK -> Credential