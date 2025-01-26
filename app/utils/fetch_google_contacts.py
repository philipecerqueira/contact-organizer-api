import requests


def fetch_google_contacts(token, params):
    response = requests.get(
        "https://people.googleapis.com/v1/people/me/connections",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
    )
    if response.status_code != 200:
        raise Exception({"code": response.status_code})
    return response.json()
