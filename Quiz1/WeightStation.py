"""WeightStation"""
def weight():
    """cal weight"""
    avg = float(input())
    w_1 = float(input())
    w_2 = float(input())
    w_3 = float(input())
    w_4 = (avg * 4) - w_1 - w_2 - w_3
    if (avg * 4) > 15000:
        print("Overweight")
    elif (avg / 2) <= w_1 <= (avg + (avg / 2)) and \
        (avg / 2) <= w_2 <= (avg + (avg / 2)) and \
        (avg / 2) <= w_3 <= (avg + (avg / 2)) and \
        (avg / 2) <= w_4 <= (avg + (avg / 2)):
        print("Pass", "%.2f" %w_4)
    else:
        print("Unbalance")
weight()
