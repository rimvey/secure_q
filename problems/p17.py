USERS = {
    "kim": {"email": "Kim@Example.com", "team": "dev"},
    "lee": {"email": "Lee@Example.com", "team": "ops"},
}


def find_user(name):
    return USERS.get(name)


def notify_address(name):
    user = find_user(name)
    return user["email"].lower()


def team_of(name):
    user = find_user(name)
    return user["team"]


def send_notice(name, text):
    address = notify_address(name)
    print("to=%s body=%s" % (address, text))
