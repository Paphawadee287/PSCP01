"""Cat Parade"""
def main():
    """main"""
    mylist = []
    newlist = []
    while True:
        cat = input()
        if cat == "END":
            break
        if cat != "IT'S A DOG":
            if ", " in cat:
                cat = cat.split(", ")
                mylist.extend(cat)
            else:
                mylist.append(cat)
        else:
            mylist.pop()
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    newlist.sort()
    for i in newlist:
        print(i, mylist.index(i)+1, mylist.count(i))
main()
