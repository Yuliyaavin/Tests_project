import os

import pytest
from dotenv import load_dotenv

from api.notes import Notes
from api.person import Person

load_dotenv()

@pytest.fixture
def user():
    return Person()

@pytest.fixture
def token(user):
    return user.get_token(os.getenv("EMAIL"), os.getenv("PASSWORD"))

@pytest.fixture
def notes():
    return Notes()

@pytest.fixture()
def new_note(token, notes):
    response = notes.create_note("lol", "kek", token=token)
    return response

@pytest.fixture()
def note_id(token, notes):
    all_notes = notes.get_notes(token=token).json()
    return max(n["id"] for n in all_notes if n["content"] == "lol" and n["title"] == "kek")

@pytest.fixture
def teardown_note(token, notes):
    notes_id = []
    yield notes_id
    for note_id in notes_id:
        notes.delete_note(note_id, token=token)

@pytest.fixture
def setup_teardown(new_note, note_id, teardown_note):
    teardown_note.append(note_id)
    yield note_id

@pytest.fixture
def second_token(user):
    return user.get_token(os.getenv("EMAIL2"), os.getenv("PASSWORD2"))