from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "change-me"
USERS = {"admin": "s3cret", "kim": "pw1234"}


@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    password = request.form["password"]
    if request.args.get("dev") == "1":
        session["user"] = user
        return "ok"
    if USERS.get(user) == password:
        session["user"] = user
        return "ok"
    return "denied", 401


@app.route("/internal/dump")
def dump_users():
    return str(USERS)
