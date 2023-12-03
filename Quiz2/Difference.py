"""Difference"""
def main(val_n, val_m):
    """main"""
    seta = set()
    setb = set()
    for _ in range(val_n):
        member_a = int(input())
        seta.add(member_a)
    for _ in range(val_m):
        member_b = int(input())
        setb.add(member_b)
    ans_set = seta.difference(setb)
    anss = sorted(ans_set)
    print(*anss)
main(int(input()), int(input()))
