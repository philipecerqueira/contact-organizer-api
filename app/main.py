import os

from flask import Flask

from app.api.auth import auth_bp
from app.api.google_contacts import google_contacts_bp
from app.api.health import health_bp
from app.utils.oauth import oauth


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "your-secret-key")

    oauth.init_app(app)
    oauth.register(
        name="google",
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        access_token_url="https://oauth2.googleapis.com/token",
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        api_base_url="https://www.googleapis.com/",
        client_kwargs={
            "scope": "https://www.googleapis.com/auth/contacts.readonly",
            "prompt": "consent",
            "access_type": "offline",
        },
    )

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(google_contacts_bp, url_prefix="/api/contact")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
