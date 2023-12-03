"""[Midterm 2020] Phone Number"""
def main():
    """main"""
    phone = input()
    country = input()
    part1 = phone[:-8]
    part2 = phone[-8:-4]
    part3 = phone[-4:]
    txt = part1
    if country == "International":
        txt = "+66"
        if len(part1) == 2:
            txt = txt + phone[1]
    print("%s" %txt + ' ' + part2 + ' ' + part3)
main()
