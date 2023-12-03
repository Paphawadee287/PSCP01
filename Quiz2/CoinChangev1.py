"""CoinChangev1"""
def main(num):
    """main"""
    res = 0
    coin = [25, 10, 5, 1]
    for i in coin:
        res += num // i
        num = num % i
    print(res)
main(int(input()))
