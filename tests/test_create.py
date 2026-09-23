class TestCreateNote:

    def test_create_note(self, token, notes, teardown_note):
        response = notes.create_note("lol", "kek", token=token)
        res_json = response.json()
        assert response.status_code == 201
        assert res_json["message"] == "Заметка создана!"

    def test_create_note_without_token(self, notes):
        response = notes.create_note("lol", "kek")
        res_json = response.json()
        assert response.status_code == 401
        assert res_json["message"] == "Token is missing!"

    def test_create_note_invalid_token(self, token, notes):
        response = notes.create_note("lol", "kek", token="False_token")
        res_json = response.json()
        assert response.status_code == 403
        assert res_json["message"] == "Token is invalid or expired!"
