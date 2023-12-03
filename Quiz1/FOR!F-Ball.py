"""FOR!F-Ball"""
def main(txt, cup1=1, cup2=0, cup3=0):
    """main"""
    for i in txt:
        if i == 'A':
            store = cup1
            cup1 = cup2
            cup2 = store
        elif i == 'B':
            store = cup2
            cup2 = cup3
            cup3 = store
        else:
            store = cup1
            cup1 = cup3
            cup3 = store
    if cup1 == 1:
        print(1)
    elif cup2 == 1:
        print(2)
    else:
        print(3)
main(input())
