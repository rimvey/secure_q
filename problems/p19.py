import socket
from flask import Flask, request, abort

app = Flask(__name__)


def is_internal(remote_addr):
    host = socket.gethostbyaddr(remote_addr)[0]
    return host.endswith(".corp.example.com")


@app.route("/admin")
def admin_page():
    if not is_internal(request.remote_addr):
        abort(403)
    return "관리자 화면"


@app.route("/")
def index():
    return "home"
