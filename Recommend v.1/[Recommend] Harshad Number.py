"""[Recommend] Harshad Number"""
def main():
    """main"""
    for _ in range(10):
        number = int(input())
        number = abs(number)
        count = 0
        for i in str(number):
            count += int(i)
        if number == 0:
            print('No')
        elif number % count == 0:
            print('Yes')
        else:
            print('No')
main()
