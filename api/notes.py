from api.base_api import BaseApi


class Notes(BaseApi):
    ENDPOINT = "api/notes"
    HEADERS = {"accept": "application/json"}
    def get_notes(self, token=None):
        headers = {**self.HEADERS, "Authorization": f"Bearer {token}" if token else None}
        return self.get(self.ENDPOINT, headers)

    def create_note(self, content, title, token=None):
        headers = {**self.HEADERS, "Authorization": f"Bearer {token}" if token else None}
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, headers, json)

    def delete_note(self, note_id, token=None):
        headers = {**self.HEADERS, "Authorization": f"Bearer {token}" if token else None}
        return self.delete(f"{self.ENDPOINT}/{note_id}", headers)
