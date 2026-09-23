from api.persons import Reg, Auth


def register_user(email, password, username):
    reg = Reg()
    resp = reg.create_user(email, password, username)
    if resp.status_code not in (201, 409):
        raise RuntimeError(f"Registration failed: {resp.status_code}")


def get_token_for(email, password):
    auth = Auth()
    auth.login(email, password)
    return auth.get_token()
