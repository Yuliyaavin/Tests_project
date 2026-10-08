import uuid


class TestCreateNote:

    def test_create_note(self, token, notes, teardown_note):
        title = uuid.uuid4().hex
        response = notes.create_note("lol", title, token=token)
        res_json = response.json()
        assert response.status_code == 201
        assert res_json["message"] == "Заметка создана!"

        teardown_note.append(notes.get_note_by_title(title, token=token))

    def test_create_note_without_token(self, notes):
        response = notes.create_note("lol", "kek")
        res_json = response.json()
        assert response.status_code == 401
        assert res_json["message"] == "Token is missing!"

    def test_create_note_invalid_token(self, notes):
        response = notes.create_note("lol", "kek", token="False_token")
        res_json = response.json()
        assert response.status_code == 403
        assert res_json["message"] == "Token is invalid or expired!"
