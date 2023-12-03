"""AndAgainAndAgainAndAgain"""
def main(txt):
    """main"""
    count = 0
    sara = ['a', 'e', 'i', 'o', 'u']
    res = []
    txt = txt.split(" ")
    for i in txt:
        for j in i:
            if j in sara:
                count += 1
        if count >= 2:
            res.append(i)
        count = 0
    res.sort()
    if len(res) == 0:
        print("Nope")
    else:
        for i in res:
            print(i)
main(input().replace(".", ""))
