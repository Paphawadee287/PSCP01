"""[Midterm 2021] Squid Game"""
def main():
    """main"""
    counta = 0
    resulta = 0
    countb = 0
    resultb = 0
    while counta < 10:
        powera = int(input())
        resulta += powera
        counta += 1
    while countb < 10:
        powerb = int(input())
        resultb += powerb
        countb += 1
    if resulta > resultb:
        print('B')
    elif resulta < resultb:
        print('A')
    else:
        print('AB')
main()
