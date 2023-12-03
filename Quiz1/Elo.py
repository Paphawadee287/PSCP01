"""Elo"""
def cal():
    """EA EB"""
    r_a = int(input())
    r_b = int(input())
    choose = input()
    if choose == 'A':
        result = 1 / (1 + 10 ** ((r_b - r_a) / 400))
    else:
        result = 1 / (1 + 10 ** ((r_a - r_b) / 400))
    print("%.2f" %result)
cal()
