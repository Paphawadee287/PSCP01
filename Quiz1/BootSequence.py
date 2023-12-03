"""BootSequence"""
def main():
    """use sep, end"""
    number = int(input())
    for i in range(1, number + 1):
        if i == number:
            print(i)
        else:
            print(i, end="_")
main()
