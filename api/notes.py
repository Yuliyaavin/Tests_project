from api.personal_api import PersonalAPI


class Notes(PersonalAPI):
    ENDPOINT = "api/notes"
    def get_notes(self, auth=True):
        return self.get(self.ENDPOINT, headers=self._headers(auth))

    def create_note(self, content, title, auth=True):
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, json=json, headers=self._headers(auth))

    def delete_note(self, note_id, auth=True):
        return self.delete(f"{self.ENDPOINT}/{note_id}", headers=self._headers(auth))

    def get_note_id_by_title(self, title):
        all_notes = self.get_notes().json()
        return next(n["id"] for n in all_notes if n["title"] == title)
