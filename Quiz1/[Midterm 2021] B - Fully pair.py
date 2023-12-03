"""[Midterm 2021] B - Fully pair?"""
def main(txt):
    """main"""
    count = 0
    paired = ""
    unmatch = ""
    for i in txt:
        if i in paired:
            continue
        count = txt.count(i)
        if count % 2 != 0:
            if count > 1:
                paired += i
            unmatch += i
        else:
            paired += i
    if unmatch == "":
        print("fully paired")
    else:
        print(unmatch)
main(input())
