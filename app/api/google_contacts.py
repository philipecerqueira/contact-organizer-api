from flask import Blueprint, jsonify, request

from app.utils import fetch_google_contacts, get_user_auth

google_contacts_bp = Blueprint("google_contacts", __name__)


@google_contacts_bp.route("/", methods=["GET"])
def get_contacts():
    """Retorna todos os contatos"""
    try:
        user = get_user_auth()
        page_token = request.args.get("pageToken")

        params = {
            "personFields": "names,emailAddresses,phoneNumbers",
            "pageSize": 50,
        }

        if page_token:
            params["pageToken"] = page_token

        data = fetch_google_contacts(user["token"], params)

        return jsonify(data)
    except Exception as e:
        print(f"CONTACT ERROR -> {str(e)}")
        error_details = e.args[0]
        if error_details["code"] == 401:
            return jsonify({"error": "User not authenticated"}), 401

        return jsonify({"error": "An error occurred during get contact"}), 500


@google_contacts_bp.route("/by-domain", methods=["GET"])
def get_by_domain():
    """Retorna contatos que tem email por domínio"""
    try:
        user = get_user_auth()
        filtered_contacts = []
        page_token = None

        while True:
            params = {
                "personFields": "emailAddresses",
                "pageSize": 1000,
            }
            if page_token:
                params["pageToken"] = page_token

            data = fetch_google_contacts(user["token"], params)
            connection_list = data.get("connections", [])

            for connection in connection_list:
                if "emailAddresses" in connection:
                    for email in connection["emailAddresses"]:
                        _, domain = email["value"].split("@")

                        domain_found = False
                        for domain_dict in filtered_contacts:
                            if domain_dict["domain"] == domain:
                                domain_dict["emails"].append(email["value"])
                                domain_found = True
                                break

                        if not domain_found:
                            filtered_contacts.append(
                                {"domain": domain, "emails": [email["value"]]}
                            )

            page_token = data.get("nextPageToken")
            if not page_token:
                break

        return jsonify(filtered_contacts)
    except Exception as e:
        print(f"CONTACT ERROR -> {str(e)}")
        error_details = e.args[0]
        if error_details["code"] == 401:
            return jsonify({"error": "User not authenticated"}), 401

        return jsonify({"error": "An error occurred during get contact"}), 500
