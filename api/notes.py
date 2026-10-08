from api.base_api import BaseApi


class Notes(BaseApi):
    ENDPOINT = "api/notes"
    def get_notes(self, token=None, with_auth=True):
        headers = self.build_headers(token, with_auth)
        return self.get(self.ENDPOINT, headers)

    def create_note(self, content, title, token=None, with_auth=True):
        headers = self.build_headers(token, with_auth)
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, headers, json)

    def delete_note(self, note_id, token=None, with_auth=True):
        headers = self.build_headers(token, with_auth)
        return self.delete(f"{self.ENDPOINT}/{note_id}", headers)

    def get_note_by_title(self, title, token=None):
        all_notes = self.get_notes(token=token).json()
        return next(n["id"] for n in all_notes if n["title"] == title)
