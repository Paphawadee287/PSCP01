"""Sequence IX"""
def main():
    """main"""
    number = int(input())
    for i in range(1, number + 1):
        for j in range(number, i, -1):
            print('  ', end=' ')
        for j in range(1, i + 1):
            print("%02d" %j, end=' ')
        for j in range(i - 1, 0, -1):
            print("%02d" %j, end=' ')
        print()
main()
