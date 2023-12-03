"""Gift II"""
def even_gift1():
    """even weight"""
    gift1 = int(input())
    gift2 = int(input())
    gift3 = int(input())
    gift4 = int(input())
    if gift1 % 2 == 0:
        print(gift1)
    elif gift2 % 2 == 0:
        print(gift2)
    elif gift3 % 2 == 0:
        print(gift3)
    elif gift4 % 2 == 0:
        print(gift4)
    else:
        pass
even_gift1()
def even_gift2():
    """even weight"""
    gift5 = int(input())
    gift6 = int(input())
    gift7 = int(input())
    gift8 = int(input())
    if gift5 % 2 == 0:
        print(gift5)
    elif gift6 % 2 == 0:
        print(gift6)
    elif gift7 % 2 == 0:
        print(gift7)
    elif gift8 % 2 == 0:
        print(gift8)
even_gift2()
"""
def loop(nam1, namx):
    '''just a loop'''
    nam = int(input())
    namx += 1
    if nam%2 == 0:
        nam1 = nam
    if namx >= 8:
        print(nam1)
        return
    loop(nam1, namx)
def main():
    '''daloop'''
    loop(0, 0)
main()
"""
"""
def main():
    weight = int(input())
    if weight % 2 == 0:
        return weight
    return main()
print(main())
"""