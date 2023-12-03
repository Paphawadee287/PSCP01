"""SumOfNumber"""
def main():
    """main"""
    summ = 0
    total = int(input())
    while summ != total:
        number = int(input())
        if number == -1:
            break
        summ += number
    print(summ)
main()
