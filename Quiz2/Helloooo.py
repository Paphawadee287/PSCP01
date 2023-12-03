"""Helloooo"""
def main(txt):
    """Helloooo"""
    check = ['a', 'e', 'i', 'o', 'u']
    res = ''
    ans1 = ''
    ind = 0
    for i in txt:
        if i in check:
            res += i
    if res == '':
        print(txt)
    else:
        for i in res:
            if res.count(i) > 1:
                ind = res.count(i)
                print(txt + res[-1]*3)
                break
        if ind < 2:
            for i in txt:
                if txt.index(i) == txt.index(res[-1]):
                    ans1 += i + res[-1]*3
                else:
                    ans1 += i
            print(ans1)
main(input())
