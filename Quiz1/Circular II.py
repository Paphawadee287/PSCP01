"""Circular II"""
def circular():
    """main"""
    import math
    var_x1 = float(input())
    var_y1 = float(input())
    radius1 = float(input())
    var_x2 = float(input())
    var_y2 = float(input())
    radius2 = float(input())
    distance = math.hypot(var_x1 - var_x2, var_y1 - var_y2)
    if distance >= radius1 + radius2:
        print("No")
    else:
        print("Yes")
circular()
    