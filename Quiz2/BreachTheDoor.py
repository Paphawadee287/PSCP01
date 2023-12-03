"""BreachTheDoor"""
def main(txt):
    """main"""
    check_len = list(filter(lambda x: len(x) > 6, txt))
    for i in check_len:
        res = ""
        for j in i:
            if j.isalpha():
                res += j
        if len(res) > 6:
            print(res, end=" ")
main(input().split(" "))
