# Install icecream for logging/debugging
from icecream import ic
ic.configureOutput(prefix='[debug] ')
ic.enable()

import credential_store

mycredential_store = credential_store.CredentialStore()

mycredential_store.add_credential("app1", ["username","user123"])
mycredential_store.add_credential("auth_token","abc123")

ic(mycredential_store.get_credential("app1"))  # Output: user123
ic(mycredential_store.get_credential("auth_token"))  # Output: abc123