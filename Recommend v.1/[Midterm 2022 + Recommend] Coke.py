"""[Midterm 2022 + Recommend] Coke"""
def coke(price, count, newprice, want):
    """coke"""
    money = 0
    if count == 0:
        money += price * want
    else:
        promotion = want // count
        money += promotion * newprice
coke(int(input()), int(input()), int(input()), int(input()))

"""
10
3
7
50
ราคาเดิม = 50*10 = 500
50 // 3 = 16
money = 16 * 7 = 112
50%3 != 0
112 + (50 - 16)*10 = 112 + 340 = 452

1
10
0
50
ราคาเดิม = 50*1 = 50
50 // 10 = 5
money = 5 * 0 = 0
50 % 10 == 0 and 50 // 10 != 0
5 - 1 = 4
0 - 0 = 0

"""