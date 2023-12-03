"""Sequence XI"""
def main(number):
    """main"""
    # for i in range(1, number + 2):
    #     for j in range(1, i + 1):
    #         print("%02d" %j, end=' ')
    #     for j in range(i - 1, 0, -1):
    #         print("%02d" %j, end=' ')
    #     print()
    for i in range(1, 2 * number):
        for j in range(1, 2 * number):
            print("{:02d}".format(min(i, j, 2 * number - i, 2 * number - j) + 1), end=' ')
        print()
main(int(input()))
