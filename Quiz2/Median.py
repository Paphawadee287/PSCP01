"""Median"""
def main(time):
    """main"""
    mylist = []
    for _ in range(time):
        number = int(input())
        mylist.append(number)
    mylist.sort()
    if time % 2 == 0:
        time1 = time // 2
        time2 = time1 - 1
        result = (mylist[time1] + mylist[time2]) / 2
    else:
        time = time // 2
        result = mylist[time]
    print("%.1f" %result)
main(int(input()))
