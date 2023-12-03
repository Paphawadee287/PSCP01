"""RockPaperScissor"""
def main():
    """Rock Paper Scissor
    A win => RS PR SP
    B win => SR RP PS 
    """
    txt = input()
    countA = 0
    countB = 0
    for i in range(0, len(txt), 2):
        if txt[i] + txt[i + 1] in ('RS' or 'PR' or 'SP'):
            countA += 1
        elif txt[i] == txt[i + 1]:
            countA += 1
            countB += 1
        else:
            countB += 1
    print(countA)
    # if countA == countB:
    #     print("DRAW", countA)
    # elif countA > countB:
    #     print('A win', "%d-%d" %(countA, countB))
    # else:
    #     print('B win', "%d-%d" %(countB, countA))
main()
