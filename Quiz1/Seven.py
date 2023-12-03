"""Seven"""
def main():
    """
    7 9 3 1 7 9 3 1 7 9
    3 1 ...
    7 9 ...
    """
    number = int(input())
    if number % 4 == 1:
        print(7)
    elif number % 4 == 2:
        print(9)
    elif number % 4 == 3:
        print(3)
    else:
        print(1)
main()
