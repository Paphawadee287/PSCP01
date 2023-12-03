"""GraderMachine"""
def find():
    """find even and summation"""
    start = int(input())
    stop = int(input())
    summ = 0
    print("pass : ", end="")
    if start < stop:
        for i in range(start, stop + 1):
            if i % 2 == 0:
                print(i, end=" ")
                summ += i
    else:
        for i in range(start, stop - 1, -1):
            if i % 2 == 0:
                print(i, end=" ")
                summ += i
    print("\nSum :", summ)
find()
