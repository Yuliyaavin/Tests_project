
class TestDeleteNote:

    def test_delete_note(self, new_note, note_id, token, notes):
        response = notes.delete_note(note_id, token=token)
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["message"] == "Note deleted!"

    def test_delete_note_without_token(self, setup_teardown, notes):
        response = notes.delete_note(setup_teardown)
        res_json = response.json()
        assert response.status_code == 401
        assert res_json["message"] == "Token is missing!"

    def test_delete_note_invalid_token(self, setup_teardown, notes):
        response = notes.delete_note(setup_teardown, token="False_token")
        res_json = response.json()
        assert response.status_code == 403
        assert res_json["message"] == "Token is invalid or expired!"

    def test_delete_note_outsider_token(self, outsider_token, setup_teardown, notes):
        response = notes.delete_note(setup_teardown, token=outsider_token)
        res_json = response.json()
        assert response.status_code == 409
        assert res_json["message"] == "Not authorized to delete this note"
