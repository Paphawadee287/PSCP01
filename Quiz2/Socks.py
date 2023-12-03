"""Socks"""
def main(sock):
    """main"""
    sock = sorted(sock)
    count = ''
    res2 = ''
    res = 0
    for i in sock:
        if i not in count:
            count += i
            nub = sock.count(i) // 2
            res += nub
            res2 += '%s ' %(i*2)*nub
    if res == 0:
        print("None")
    else:
        print(res2)
    print(res)
main(input())
    