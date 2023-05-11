# Application Credential Manager
A credential (username/password) manager for applications.

## Project Status
Currently this is just an idea.

## Background
Applications need password and other credentials to access databases, REST APIs, and other resources.  This project acts as a central manager for housing those credentials and providing access to authorized applications.

Typically, developers follow some consistent practice for managing these credentials, but they often differ even within the same organization.  This project aims to create a consistent, secure, and easy to use method for standardizing the method of managing credentials.

## Features
- Store/Update credentials 
  - username/password pairs
  - authorization tokens

- Register applications
  - each application gets registered individually

- Grant/Revoke credentials
  - registered applications are provisioned only specific credentials needed
