"""Triangle I"""
def triangle(num1, num2):
    """main"""
    if num1 > num2:
        return num1
    return num2

def main():
    """input and result"""
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
    highest = triangle(triangle(side1, side2), side3)
    create = (side1 ** 2 + side2 ** 2 + side3 ** 2 - highest ** 2) ** 0.5
    if abs(create - highest) <= 0.01:
        print("Yes")
    else:
        print("No")
main()
    # highest = 0
    # if highest < side1:
    #     highest = side1
    #     create = (side2 ** 2 + side3 ** 2) ** 0.5
    # if highest < side2:
    #     highest = side2
    #     create = (side1 ** 2 + side3 ** 2) ** 0.5
    # if highest < side3:
    #     highest = side3
    #     create = (side1 ** 2 + side2 ** 2) ** 0.5

    # if abs(create - highest) <= 0.01:
    #     print("Yes")
    # else:
    #     print("No")
