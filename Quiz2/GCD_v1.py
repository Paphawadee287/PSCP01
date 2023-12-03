"""GCD_v1"""
def main(num1, num2):
    """main"""
    for i in range(1, min(num1, num2)+1):
        if num1%i == 0 and num2%i == 0:
            res = i
    print(res)
main(int(input()), int(input()))

# def main(val1, val2):
#     """main"""
#     while val2:
#         val1, val2 = val2, val1 % val2
#     print(val1)
# main(int(input()), int(input()))
