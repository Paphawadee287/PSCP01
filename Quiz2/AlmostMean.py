"""AlmostMean"""
def main(val_n):
    """main"""
    mylist1 = []
    mylist2 = []
    total = 0
    for score in range(val_n):
        score = input()
        mylist1.append(score.split()[0])
        mylist2.append(score.split()[-1])
        total += float(score.split()[-1])
    total /= val_n
    res = total * 2
    for j, i in enumerate(mylist2, start=0):
        if total < float(i):
            continue
        elif total - float(i) < abs(total - float(res)):
            res = i
            res2 = j
    print("%s	%s" %(mylist1[res2], res))
main(int(input()))
