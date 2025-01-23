from authlib.integrations.flask_client import OAuth

oauth = OAuth()


def get_google_client():
    """Obtém o cliente OAuth do Google dinamicamente."""
    return oauth.create_client("google")
