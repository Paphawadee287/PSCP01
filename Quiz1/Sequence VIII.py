"""Sequence VIII"""
def main():
    """main"""
    number = int(input())
    for i in range(1, number + 1):
        print('   ' * (number - i), end="")
        for j in range(1, i + 1):
            if j > i:
                break
            print('%02d ' %j, end="")
        print()

main()
