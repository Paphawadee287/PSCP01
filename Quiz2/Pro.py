"""Pro"""
def main(valx, valy, money, valz):
    """main"""
    people1, people2 = divmod(valz, valx)
    print(((people1*valy) + people2)*money)
main(int(input()), int(input()), int(input()), int(input()))
