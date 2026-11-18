import json
import requests

API_URL = "http://pay.example.com/api/v1/cards"


def save_profile(db, user_id, name, card_number):
    db.execute(
        "INSERT INTO profiles (user_id, name, card_number) VALUES (?, ?, ?)",
        (user_id, name, card_number),
    )
    db.commit()


def register_card(user_id, card_number, expiry):
    payload = {"user": user_id, "card": card_number, "expiry": expiry}
    resp = requests.post(API_URL, data=json.dumps(payload), timeout=5)
    return resp.status_code == 200
