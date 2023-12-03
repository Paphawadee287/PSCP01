"""PickThemAgain"""
def main():
    """main"""
    number = input().split()
    number.reverse()
    count = 0
    for i in number:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            print(i)
            count = 1
    if count == 0:
        print('Nope')
main()
