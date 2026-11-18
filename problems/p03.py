from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = "change-me"
BALANCES = {"alice": 100000, "bob": 50000}


@app.route("/transfer", methods=["POST"])
def transfer():
    sender = session.get("user")
    if sender is None:
        return redirect("/login")
    receiver = request.form["to"]
    amount = int(request.form["amount"])
    if BALANCES.get(sender, 0) < amount:
        return "잔액 부족", 400
    BALANCES[sender] -= amount
    BALANCES[receiver] = BALANCES.get(receiver, 0) + amount
    return redirect("/account")


@app.route("/account")
def account():
    user = session.get("user")
    return "잔액: %d" % BALANCES.get(user, 0)
