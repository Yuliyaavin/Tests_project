from api.base_api import BaseApi


class RegAuth(BaseApi):
    def create_user(self, email, password, username):
        json = {"email": email, "password": password, "username": username}
        return self.post("api/register", self.build_headers(), json=json)

    def login(self, email, password):
        json = {"email": email, "password": password}
        self.resp_login = self.post("api/login", self.build_headers(), json=json)
        return self.resp_login

    def get_token(self, email, password):
        return self.login(email, password).json()["token"]

