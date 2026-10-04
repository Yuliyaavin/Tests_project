import os

import pytest
from dotenv import load_dotenv

from api.notes import Notes
from api.persons import RegAuth

load_dotenv()

@pytest.fixture(scope='function')
def user():
    return RegAuth()

@pytest.fixture(scope="session")
def register_user():
    reg_auth = RegAuth()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    username = os.getenv("USERNAME")
    resp = reg_auth.create_user(email, password, username)
    if resp.status_code not in (201, 409):
        raise RuntimeError(f"Registration failed: {resp.status_code}")
    return {"email": email, "password": password}

@pytest.fixture
def token(user, register_user):
    user.login(register_user["email"], register_user["password"])
    return user.get_token()

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
    for p in notes_id:
        notes.delete_note(p, token=token)

@pytest.fixture
def setup_teardown(new_note, note_id, teardown_note):
    teardown_note.append(note_id)
    yield note_id

@pytest.fixture
def outsider_token():
    reg_auth2 = RegAuth()
    email2 = os.getenv("EMAIL2")
    password2 = os.getenv("PASSWORD2")
    username2 = os.getenv("USERNAME2")
    resp = reg_auth2.create_user(email2, password2, username2)
    if resp.status_code not in (201, 409):
        raise RuntimeError(f"Registration failed: {resp.status_code}")
    reg_auth2.login(email2, password2)
    return reg_auth2.get_token()
