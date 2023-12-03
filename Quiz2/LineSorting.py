"""LineSorting"""
def meesage(time):
    """message"""
    mylist = []
    for _ in range(time):
        txt = input()
        mylist.append(txt)
    mylist.sort(key=len)
    for j in mylist:
        print(j)
meesage(int(input()))
