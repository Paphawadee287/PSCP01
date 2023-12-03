"""[Midterm 2020] BigFrame"""
def create_frame(txt):
    """main"""
    maxlen = 0
    #หาจำนวนตัวอักษรที่มากที่สุด
    for i in txt:
        if len(i) > maxlen:
            maxlen = len(i)
    print('*' * (maxlen+4))
    #print txt
    for i in txt:
        print('* ' + i + ' ' * (maxlen - len(i)) + ' *')
    print('*' * (maxlen+4))
create_frame([input().strip() for _ in range(5)])

# def create_frame():
#     """main"""
#     txt1 = input().strip(" ")
#     txt2 = input().strip(" ")
#     txt3 = input().strip(" ")
#     txt4 = input().strip(" ")
#     txt5 = input().strip(" ")
#     val_max = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
#     print('*' * (val_max + 4))
#     print("* %s" %txt1 + " " * (val_max - len(txt1)) + " *")
#     print("* %s" %txt2 + " " * (val_max - len(txt2)) + " *")
#     print("* %s" %txt3 + " " * (val_max - len(txt3)) + " *")
#     print("* %s" %txt4 + " " * (val_max - len(txt4)) + " *")
#     print("* %s" %txt5 + " " * (val_max - len(txt5)) + " *")
#     print('*' * (val_max + 4))
# create_frame()
