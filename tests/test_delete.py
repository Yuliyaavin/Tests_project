
class TestDeleteNote:

    def test_delete_note(self, note_id, notes):
        response = notes.delete_note(note_id)
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["message"] == "Note deleted!"

    def test_delete_note_without_token(self, setup_teardown, notes):
        response = notes.delete_note(setup_teardown, auth=False)
        res_json = response.json()
        assert response.status_code == 401
        assert res_json["message"] == "Token is missing!"

    def test_delete_note_invalid_token(self, setup_teardown, notes_invalid_token):
        response = notes_invalid_token.delete_note(setup_teardown)
        res_json = response.json()
        assert response.status_code == 403
        assert res_json["message"] == "Token is invalid or expired!"

    def test_delete_note_outsider_token(self, notes_outsider, setup_teardown):
        response = notes_outsider.delete_note(setup_teardown)
        res_json = response.json()
        assert response.status_code == 409
        assert res_json["message"] == "Not authorized to delete this note"
