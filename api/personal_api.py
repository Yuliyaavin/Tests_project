from api.base_api import BaseApi


class PersonalAPI(BaseApi):
    def __init__(self, token):
        self.token = token
    def _headers(self, auth=True):
        headers = {**self.HEADERS}
        if auth:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers
