class User:
    def __init__(self, login):
        self.login = login

    def getLogin(self):
        return self.login

    def print(self):
        print(self.login)