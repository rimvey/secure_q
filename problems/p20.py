import base64
import pickle
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/prefs", methods=["GET", "POST"])
def prefs():
    if request.method == "POST":
        data = {"theme": request.form.get("theme", "light")}
        resp = make_response("saved")
        resp.set_cookie("prefs", base64.b64encode(pickle.dumps(data)).decode())
        return resp
    raw = request.cookies.get("prefs")
    if raw is None:
        return "light"
    data = pickle.loads(base64.b64decode(raw))
    return data["theme"]
