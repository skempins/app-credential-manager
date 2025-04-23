class CredentialStore:
    """A class to manage credentials in a secure store."""
    
    def __init__(self):
        self.credentials = {}

    def add_credential(self, key, value):
        """Add a new credential to the store."""
        self.credentials[key] = value

    def get_credential(self, key):
        """Retrieve a credential from the store."""
        return self.credentials.get(key)

    def remove_credential(self, key):
        """Remove a credential from the store."""
        if key in self.credentials:
            del self.credentials[key]