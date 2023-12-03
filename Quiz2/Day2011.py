"""Day2011"""
def main(day, month):
    """main"""
    year = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    weeks = \
    {0:'Friday', 1:'Saturday', 2:'Sunday', 3:'Monday', 4:'Tuesday', 5:'Wednesday', 6:'Thursday'}
    res = 0
    for i in range(1, month):
        res += year[i]
    res = (res+day)%7
    if res in weeks.keys():
        print(weeks[res])
main(int(input()), int(input()))
