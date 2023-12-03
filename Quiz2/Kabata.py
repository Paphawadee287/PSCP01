"""Kabata"""
def kabata():
    """find ka ba ta bakka"""
    check = ["bakka", "ka", "ba", "ta"]
    for _ in range(int(input())):
        txt = input()
        if txt.find("baka") != -1:
            print("no")
        else:
            for word in check:
                txt = txt.replace(word, " ")
            if txt.isspace():
                print("yes")
            else:
                print("no")
kabata()
