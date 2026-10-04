class TestGetNote:

    def test_get_note(self, setup_teardown, token, notes):
        response = notes.get_notes(token=token)
        res_json = response.json()
        assert response.status_code == 200
        note = next(n for n in res_json if n["id"] == setup_teardown)
        assert note["content"] == "lol"
        assert note["title"] == "kek"
        assert note["id"] == setup_teardown

    def test_get_note_without_token(self, notes):
        response = notes.get_notes()
        res_json = response.json()
        assert response.status_code == 401
        assert res_json["message"] == "Token is missing!"

    def test_get_note_invalid_token(self, notes):
        response = notes.get_notes(token="False_token")
        res_json = response.json()
        assert response.status_code == 403
        assert res_json["message"] == "Token is invalid or expired!"
