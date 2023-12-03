"""Water"""
def main(month, paymax, valb, payb, vald):
    """main"""
    res = 0
    for _ in range(month):
        vali = float(input())
        if vali <= valb:
            pay = vali*paymax
        else:
            pay = ((vali - valb)*payb)+(paymax*valb)
        if pay > vald:
            res += pay
        else:
            res += 0
    print('%.2f' %res)
main(int(input()), float(input()), float(input()), float(input()), float(input()))
