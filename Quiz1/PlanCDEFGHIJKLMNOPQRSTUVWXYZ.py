"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def find_option(option, number1, number2, number3):
    """main"""
    if option == "Ascend":
        print("%.2f, %.2f, %.2f" %(number3, number2, number1), sep=",")
    else:
        print("%.2f, %.2f, %.2f" %(number1, number2, number3), sep=",")

def main():
    """main"""
    option = input()
    number1 = float(input())
    number2 = float(input())
    number3 = float(input())
    if number1 < number2:
        number1, number2 = number2, number1
    if number1 < number3:
        number1, number3 = number3, number1
    if number2 < number3:
        number2, number3 = number3, number2
    find_option(option, number1, number2, number3)
main()
