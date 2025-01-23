from flask import Blueprint, jsonify, session, url_for

from app.utils.oauth import get_google_client

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login():
    try:
        google = get_google_client()
        redirect_uri = url_for("auth.callback", _external=True)
        return google.authorize_redirect(redirect_uri)
    except Exception as e:
        print(f"LOGIN ERROR -> {str(e)}")
        return jsonify({"error": "An error occurred during login"}), 500


@auth_bp.route("/callback")
def callback():
    try:
        google = get_google_client()
        token = google.authorize_access_token()

        if not token:
            return jsonify({"error": "Failed to authorize"}), 400

        session["user"] = {
            "token": token.get("access_token"),
            "token_expires_at": token.get("expires_at"),
        }

        return jsonify({"message": "Login successful", "user": session["user"]})
    except Exception as e:
        print(f"CALLBACK ERROR -> {str(e)}")
        return jsonify({"error": "An error occurred during the callback"}), 500


@auth_bp.route("/logout")
def logout():
    try:
        session.pop("user", None)
        return jsonify({"message": "Logged out successfully"})
    except Exception as e:
        print(f"LOGOUT ERROR -> {str(e)}")
        return jsonify({"error": "An error occurred during the logout"}), 500
