from flask import session


def get_user_auth():
    user = session.get("user")
    if not user or not user.get("token"):
        raise Exception({"code": 401, "message": "User not authenticated"})
    return user
