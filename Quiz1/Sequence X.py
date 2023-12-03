"""Sequence X"""
def main():
    """main"""
    number = int(input())
    for i in range(1, number):
        for j in range(number, i, -1):
            print('  ', end=' ')
        for j in range(1, i + 1):
            print("%02d" %j, end=' ')
        for j in range(i - 1, 0, -1):
            print("%02d" %j, end=' ')
        print()
    for k in range(number, 0, -1):
        for lol in range(number, k, -1):
            print('  ', end=' ')
        for lol in range(1, k + 1):
            print("%02d" %lol, end=' ')
        for lol in range(k - 1, 0, -1):
            print("%02d" %lol, end=' ')
        print()
main()
