import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_PATH = "shop.db"


def get_conn():
    return sqlite3.connect(DB_PATH)


@app.route("/orders")
def list_orders():
    customer = request.args.get("customer", "")
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT id, item, price FROM orders WHERE customer = '" + customer + "'"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "item": r[1], "price": r[2]} for r in rows])
