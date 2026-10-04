class TestCreateNote:

    def test_create_note(self, token, notes, teardown_note):
        response = notes.create_note("lol", "kek", token=token)
        res_json = response.json()
        assert response.status_code == 201
        assert res_json["message"] == "Заметка создана!"

        all_notes = notes.get_notes(token=token).json()
        note_id = max(n["id"] for n in all_notes if n["content"] == "lol" and n["title"] == "kek")
        teardown_note.append(note_id)

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
