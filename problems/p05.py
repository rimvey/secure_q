from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "change-me"
USERS = {"admin": "9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee684"}


def check_password(user, password):
    import hashlib
    stored = USERS.get(user)
    return stored is not None and hashlib.sha1(password.encode()).hexdigest() == stored


@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    password = request.form["password"]
    if check_password(user, password):
        session["user"] = user
        return "로그인 성공"
    return "로그인 실패", 401
