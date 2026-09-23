from api.base_api import BaseApi


class Reg(BaseApi):
    ENDPOINT = "api/register"
    def create_user(self, email, password, username):
        json = {"email": email, "password": password, "username": username}
        self.resp_user = self.post(self.ENDPOINT, BaseApi.HEADERS, json=json)
        return self.resp_user


class Auth(BaseApi):
    ENDPOINT = "api/login"
    HEADERS = {"accept": "application/json"}
    def login(self, email, password):
        json = {"email": email, "password": password}
        self.resp_login = self.post(self.ENDPOINT, self.HEADERS, json=json)
        return self.resp_login

    def get_token(self):
        return self.resp_login.json()["token"]
