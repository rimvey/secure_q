import logging
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(filename="auth.log", level=logging.INFO)
log = logging.getLogger("auth")


def create_user(name, password):
    return {"name": name, "password_hash": hash(password)}


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    password = request.form["password"]
    log.info("signup request name=%s password=%s", name, password)
    user = create_user(name, password)
    log.info("user created: %s", user["name"])
    return "가입 완료"
