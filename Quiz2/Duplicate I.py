"""Duplicate I"""
def main(val_m, val_n):
    """main"""
    group1 = set()
    group2 = set()
    for _ in range(val_m):
        group1.add(int(input()))
    for _ in range(val_n):
        group2.add(int(input()))
    ans_set = group1.intersection(group2)
    if ans_set == set():
        print('Nope')
    else:
        anss = sorted(ans_set, reverse=True)
        print(*anss, sep="\n")
main(int(input()), int(input()))
