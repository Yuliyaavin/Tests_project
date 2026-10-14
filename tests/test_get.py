class TestGetNotes:

    def test_get_notes(self, setup_teardown, notes):
        response = notes.get_notes()
        res_json = response.json()
        assert response.status_code == 200
        assert len(res_json) > 0

    def test_get_notes_without_token(self, notes):
        response = notes.get_notes(auth=False)
        res_json = response.json()
        assert response.status_code == 401
        assert res_json["message"] == "Token is missing!"

    def test_get_notes_invalid_token(self, notes_invalid_token):
        response = notes_invalid_token.get_notes()
        res_json = response.json()
        assert response.status_code == 403
        assert res_json["message"] == "Token is invalid or expired!"
