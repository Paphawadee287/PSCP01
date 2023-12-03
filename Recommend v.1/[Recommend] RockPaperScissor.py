"""[Recommend] RockPaperScissor"""
def rps():
    """
    A win = SP Rs PR
    """
    txt = input()
    counta = 0
    countb = 0
    for i in range(0, len(txt), 2):
        result = str(txt[i]) + str(txt[i + 1])
        if result in ('SP', 'RS', 'PR'):
            counta += 1
        elif result in ('PS', 'SR', 'RP'):
            countb += 1
    if counta == countb:
        print("DRAW %d" %counta)
    elif counta > countb:
        print("A win %d-%d" %(counta, countb))
    else:
        print("B win %d-%d" %(countb, counta))
rps()
