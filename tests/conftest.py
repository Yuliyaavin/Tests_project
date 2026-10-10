import os
import uuid

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
def notes(token):
    return Notes(token)

@pytest.fixture()
def note_title():
    return uuid.uuid4().hex

@pytest.fixture()
def note_id(notes, note_title):
    notes.create_note("lol", note_title)
    return notes.get_note_by_title(note_title)

@pytest.fixture
def teardown_note(notes):
    notes_id = []
    yield notes_id
    for n_id in notes_id:
        notes.delete_note(n_id)

@pytest.fixture
def setup_teardown(note_id, teardown_note):
    teardown_note.append(note_id)
    yield note_id

@pytest.fixture
def notes_invalid_token():
    return Notes("False_token")

@pytest.fixture
def second_token(user):
    return user.get_token(os.getenv("EMAIL2"), os.getenv("PASSWORD2"))

@pytest.fixture
def notes_outsider(second_token):
    return Notes(second_token)
