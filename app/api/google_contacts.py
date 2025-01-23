import requests
from flask import Blueprint, jsonify, session

google_contacts_bp = Blueprint("google_contacts", __name__)


@google_contacts_bp.route("/", methods=["GET"])
def get_contacts():
    """Retorna todos os contatos"""
    try:
        user = session.get("user")
        if not user or not user.get("token"):
            return jsonify({"error": "User not authenticated"}), 401

        response = requests.get(
            "https://people.googleapis.com/v1/people/me/connections",
            headers={"Authorization": f"Bearer {user['token']}"},
            params={"personFields": "names,emailAddresses,phoneNumbers,organizations"},
        )

        if response.status_code != 200:
            raise Exception(response.json())

        contacts = response.json().get("connections", [])
        return jsonify(contacts)
    except Exception as e:
        print(f"CONTACT ERROR -> {str(e)}")
        return jsonify({"error": "An error occurred during get contact"}), 500
