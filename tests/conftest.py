import pytest
import os
from dotenv import load_dotenv
load_dotenv()

#from api.persons import Reg
from api.notes import Notes
from helper.helper_person import get_token_for, register_user


@pytest.fixture(scope="session")
def user():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    username = os.getenv("USERNAME")
    register_user(email, password, username)
    return {"email": email, "password": password}

#@pytest.fixture(scope="session")
#def user():
#    reg = Reg()
#    reg.create_user("yulia_shpylia@test.com", "yuliashpylia", "yulia_shpylia")
#    return {"email": "yulia_shpylia@test.com", "password": "yuliashpylia", "username": "yulia_shpylia"}

@pytest.fixture
def notes():
    return Notes()

@pytest.fixture
def token(user):
    return get_token_for(user["email"], user["password"])

@pytest.fixture()
def new_note(token, notes):
    response = notes.create_note("lol", "kek", token=token)
    return response

@pytest.fixture()
def note_id(token, new_note, notes):
    all_notes = notes.get_notes(token=token).json()
    return max(n["id"] for n in all_notes)

#@pytest.fixture
#def note_id(token,notes):
 #   resp = notes.create_note("content", "title", token=token)
 #   note_id = resp.json()["id"]
 #   yield note_id

#@pytest.fixture
#def note_id(token, notes):
 #   notes.create_note("content", "title", token=token)
 #   all_notes = notes.get_notes(token=token).json()
  #  note_id = max(all_notes, key=lambda n: n["id"])["id"]
   # yield note_id

@pytest.fixture
def teardown_note(token,notes):
    notes_id = []
    yield notes_id
    for p in notes_id:
        notes.delete_note(p, token=token)

@pytest.fixture
def setup_teardown(note_id, teardown_note):
    teardown_note.append(note_id)
    yield note_id
