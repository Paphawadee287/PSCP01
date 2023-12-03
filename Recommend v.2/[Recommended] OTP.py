"""[Recommended] OTP"""
def main():
    """main"""
    while True:
        otp = input()
        if otp == '0':
            break
        count_num = [otp.count(str(i)) for i in range(10)]
        if len(otp) == 4 and count_num.count(2) == 1:
            print("Valid")
        elif len(otp) == 6 and (count_num.count(2) == 2 or count_num.count(3) == 1):
            print('Valid')
        elif len(otp) == 8 and (count_num.count(2) == 3 or count_num.count(3) == 2):
            print("Valid")
        else:
            print("Invalid")

main()
