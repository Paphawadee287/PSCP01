"""Helloooo"""
def main(txt):
    """main"""
    check = ['a', 'e', 'i', 'o', 'u']
    count = ''
    for i in txt:
        if i in check:
            count += i
    if count == '':
        print(txt)
    else:
        txt = list(txt[::-1])
        txt.insert(txt.index(count[-1]), count[-1]*3)
        txt = txt[::-1]
        for i in txt:
            print(i, end="")
main(input())
