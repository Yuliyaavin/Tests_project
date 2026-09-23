from api.persons import Auth


def get_token_for(email, password):
    auth = Auth()
    auth.login(email, password)
    return auth.get_token()
