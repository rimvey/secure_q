import traceback
import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/member")
def member():
    member_id = request.args.get("id", "0")
    try:
        conn = sqlite3.connect("members.db")
        row = conn.execute("SELECT name, grade FROM members WHERE id = ?", (member_id,)).fetchone()
        return "%s (%s)" % (row[0], row[1])
    except Exception as e:
        return "오류 발생\n" + traceback.format_exc(), 500
