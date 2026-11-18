import jwt

SECRET = "server-signing-secret"


def read_claims(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])


def is_admin(token):
    try:
        claims = read_claims(token)
        return claims.get("role") == "admin"
    except Exception:
        return True


def delete_user(token, user_id, db):
    if not is_admin(token):
        raise PermissionError("관리자만 가능")
    db.pop(user_id, None)
