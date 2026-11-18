import ctypes

MAX_STOCK = 1000


def total_price(unit_price, quantity):
    total = ctypes.c_int32(unit_price * quantity).value
    return total


def checkout(cart, wallet):
    amount = 0
    for unit_price, quantity in cart:
        amount += total_price(unit_price, quantity)
    if wallet < amount:
        raise ValueError("잔액 부족")
    return wallet - amount


if __name__ == "__main__":
    print(checkout([(70000, 40000)], 5000))
