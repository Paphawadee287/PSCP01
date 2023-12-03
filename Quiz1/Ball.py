"""Ball"""
def ball():
    """ball"""
    high = float(input())
    count = 0
    while high >= 0.01:
        high = (high * 3) / 5
        if high < 0.01:
            break
        count += 1
    print(count)
ball()
