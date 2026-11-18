from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "change-me"

current_user = None
current_profile = {}


@app.route("/login", methods=["POST"])
def login():
    global current_user, current_profile
    current_user = request.form["user"]
    current_profile = {"name": current_user, "email": current_user + "@example.com"}
    return "ok"


@app.route("/profile")
def profile():
    return "%s / %s" % (current_profile["name"], current_profile["email"])
