import requests


class BaseApi:
    BASE_URL = "http://185.240.103.201:8000"
    HEADERS = {"accept": "application/json"}

    def get(self, endpoint, headers=None, **kwargs):
        return requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, **kwargs)

    def post(self, endpoint, headers=None, json=None, **kwargs):
        return requests.post(f"{self.BASE_URL}/{endpoint}", json=json, headers=headers, **kwargs)

    def delete(self, endpoint, headers=None, **kwargs):
        return requests.delete(f"{self.BASE_URL}/{endpoint}", headers=headers, **kwargs)
