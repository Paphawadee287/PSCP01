"""[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main():
    """main"""
    val_x1 = int(input())
    val_x2 = int(input())
    val_x3 = int(input())
    val_x4 = int(input())
    val_y1 = int(input())
    val_y2 = int(input())
    val_y3 = int(input())
    val_y4 = int(input())
    res1 = math.ceil(val_x1 / val_y1)
    res2 = math.ceil(val_x2 / val_y2)
    res3 = math.ceil(val_x3 / val_y4)
    res4 = math.ceil(val_x4 / val_y3)
    most = res1
    if most < res2:
        most = res2
    if most < res3:
        most = res3
    if most < res4:
        most = res4
    print(most)
main()
