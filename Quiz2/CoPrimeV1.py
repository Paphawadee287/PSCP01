"""CoPrimeV1"""
def main(val1, val2):
    """main"""
    while val2:
        val1, val2 = val2, val1 % val2
    if val1 == 1:
        print('YES', val1, sep="\n")
    else:
        print('NO', val1, sep="\n")
main(int(input()), int(input()))
