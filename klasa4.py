class UserAccount:
    def __init__(self, user, passwd):
        self._username = user
        self._password = passwd

    def get_username(self):
        return self._username

    def set_username(self, user):
        self._username = user

    def get_password(self):
        return self._password

    def set_username(self, passwd):
        self._password = passwd


