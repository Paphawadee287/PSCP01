"""LetterFrequency"""
def main(message):
    """main"""
    txt = []
    maxx = 0
    res = ""
    for i in message:
        if i not in txt:
            total = message.count(i)
            txt.append(i)
        if maxx < total:
            maxx = total
            res = i
    print(res)
main(input().lower().replace(" ", ""))
