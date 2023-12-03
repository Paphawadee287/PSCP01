"""Sequence V"""
def main():
    """main"""
    number = int(input())
    count = 7
    while number > 0:
        if count >= 1:
            print(number, end=" ")
            number -= 1
            count -= 1
        else:
            print()
            count = 7
main()
