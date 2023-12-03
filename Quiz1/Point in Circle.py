"""Point in Circle"""
def cal_circle(var_x, var_y, radius, var_x0, var_y0):
    """circle"""
    point = ((var_x - var_x0) ** 2 + (var_y - var_y0) ** 2) ** 0.5
    if point <= radius:
        return "Yes"
    return "No"

def main():
    """input"""
    var_x = float(input())
    var_y = float(input())
    radius = float(input())
    var_x0 = float(input())
    var_y0 = float(input())
    print(cal_circle(var_x, var_y, radius, var_x0, var_y0))
main()
