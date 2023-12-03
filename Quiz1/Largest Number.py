"""Largest Number"""
def check(number1, number2, number3):
    """
    1 + 2 + 3
    1 + 3 + 2
    2 + 1 + 3
    2 + 3 + 1
    3 + 1 + 2
    3 + 2 + 1
    """
    ans1 = str(number1) + str(number2) + str(number3)
    ans2 = str(number1) + str(number3) + str(number2)
    ans3 = str(number2) + str(number1) + str(number3)
    ans4 = str(number2) + str(number3) + str(number1)
    ans5 = str(number3) + str(number1) + str(number2)
    ans6 = str(number3) + str(number2) + str(number1)
    largest = int(ans1)
    if int(ans2) > int(largest):
        largest = ans2
    if int(ans3) > int(largest):
        largest = ans3
    if int(ans4) > int(largest):
        largest = ans4
    if int(ans5) > int(largest):
        largest = ans5
    if int(ans6) > int(largest):
        largest = ans6
    return largest
def main(number1, number2, number3):
    """main"""
    print(check(number1, number2, number3))
main(int(input()), int(input()), int(input()))
