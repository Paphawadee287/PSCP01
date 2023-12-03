"""MissingNumber"""
def main(val_n):
    """main"""
    num = set()
    mynum = set()
    for i in range(1, val_n + 1):
        num.add(i)
    while True:
        num2 = int(input())
        if num2 == 0:
            break
        mynum.add(num2)
    missing = num.difference(mynum)
    missing1 = sorted(missing)
    print(*missing1, sep="\n")
main(int(input()))
