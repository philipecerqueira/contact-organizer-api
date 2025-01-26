import os

from flask import Flask
from flask_cors import CORS

from app.api import auth_bp, google_contacts_bp, health_bp
from app.utils import oauth


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "your-secret-key")
    app.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SECURE=False,  # TODO: Quando for https alterar para True
        SESSION_COOKIE_SAMESITE="Lax",
    )

    CORS(
        app,
        supports_credentials=True,
        origins=["http://localhost:8080", "http://127.0.0.1:8080"],
    )

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
