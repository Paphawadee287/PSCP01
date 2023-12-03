"""[Midterm 2020] Books"""
import math
def main(val_n, val_k, val_x, val_y):
    """main"""
    page = 0
    days = 0
    count = 0
    while val_n != count:
        cal = math.ceil(val_k * val_x / val_y)
        if cal >= val_k:
            break
        page += cal
        if page >= val_k:
            count += 1
            page = 0
        val_x += 1
        val_y += 1
        days += 1
    days += val_n - count
    print(days)
main(int(input()), int(input()), int(input()), int(input()))
