import threading
import time

balance = 1000


def withdraw(amount):
    global balance
    if balance >= amount:
        time.sleep(0.01)
        balance -= amount
        return True
    return False


def run():
    threads = [threading.Thread(target=withdraw, args=(800,)) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(balance)


if __name__ == "__main__":
    run()
