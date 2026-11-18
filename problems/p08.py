import hashlib
import random
import string


def make_reset_token(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def register(db, name, password):
    db[name] = {
        "password": hash_password(password),
        "reset_token": make_reset_token(),
    }
    return db[name]["reset_token"]
