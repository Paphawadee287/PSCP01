"""[Midterm 2020] Pringles"""
def main(can1, chip, can2, finger):
    """main"""
    chipincan = chip[finger:].count(")")
    eatchip = chip[:finger].count(")")
    print(eatchip)
    if chipincan == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(can1)
    print(" " * finger + chip[finger:])
    print(can2)
main(input(), input(), input(), int(input()))
