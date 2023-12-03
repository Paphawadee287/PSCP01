"""Restaurant"""
def main(vala, valb, valc, vald):
    """main"""
    new_pay = (vala + vald) * ((100 - valc) / 100)
    if new_pay > vala and (vala + vald) >= valb:
        print("No %.3f" %(new_pay - vala))
    elif new_pay < vala and (vala + vald) >= valb:
        print("Yes %.3f" %(vala - new_pay))
    else:
        print('Yes')
main(float(input()), float(input()), float(input()), float(input()))
