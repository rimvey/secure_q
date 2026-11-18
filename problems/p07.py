import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

SECRET_KEY = b"payment-key-2024"
IV = b"0000000000000000"


def encrypt_card(card_number: str) -> str:
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
    padded = pad(card_number.encode("utf-8"), AES.block_size)
    return base64.b64encode(cipher.encrypt(padded)).decode("ascii")


def charge(card_number: str, amount: int) -> dict:
    token = encrypt_card(card_number)
    return {"token": token, "amount": amount}
