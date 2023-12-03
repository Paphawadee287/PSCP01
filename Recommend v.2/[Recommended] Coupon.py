"""[Recommended] Coupon"""
def main(pay, rec1, rec2):
    """main"""
    if pay < float(rec1[1]) and pay < float(rec2[1]):
        print("Nope")
    elif pay < float(rec1[1]):
        print('2 %.1f' %(((100 - float(rec2[0])) / 100) * pay))
    elif pay < float(rec2[1]):
        print('1 %.1f' %(pay - float(rec1[0])))
    else:
        coupon1 = pay - float(rec1[0])
        coupon2 = ((100 - float(rec2[0])) / 100) * pay
        if coupon1 == coupon2:
            if float(rec1[1]) == float(rec2[1]):
                print('1 %.1f' %coupon1)
            elif float(rec1[1]) < float(rec2[1]):
                print('1 %.1f' %coupon1)
            else:
                print('2 %.1f' %coupon2)
        elif coupon1 < coupon2:
            print('1 %.1f' %coupon1)
        else:
            print('2 %.1f' %coupon2)
main(float(input()), input().split(), input().split())
    