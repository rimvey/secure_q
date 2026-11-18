import os
from flask import Flask, request, send_file, abort

app = Flask(__name__)
BASE_DIR = "/srv/reports"


@app.route("/reports")
def list_reports():
    return "\n".join(sorted(os.listdir(BASE_DIR)))


@app.route("/download")
def download():
    name = request.args.get("name", "")
    path = os.path.join(BASE_DIR, name)
    if not os.path.exists(path):
        abort(404)
    return send_file(path)
