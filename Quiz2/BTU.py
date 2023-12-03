"""BTU"""
def check1(vala):
    """check"""
    if 100 <= vala <= 150:
        total = 5000
    elif 151 <= vala <= 250:
        total = 6000
    elif 251 <= vala <= 300:
        total = 7000
    elif 301 <= vala <= 350:
        total = 8000
    elif 350 <= vala <= 400:
        total = 9000
    elif 401 <= vala <= 450:
        total = 10000
    else:
        total = 12000
    return total
def check2(vala):
    """check"""
    if 551 <= vala <= 700:
        total = 14000
    elif 701 <= vala <= 1000:
        total = 18000
    elif 1001 <= vala <= 1200:
        total = 21000
    elif 1201 <= vala <= 1400:
        total = 23000
    elif 1401 <= vala <= 1500:
        total = 24000
    elif 1501 <= vala <= 2000:
        total = 30000
    else:
        total = 34000
    return total
def check3(sun):
    """check"""
    if sun == "facing the sun":
        total = 1.1
    elif sun == "shaded":
        total = 0.9
    else:
        total = 1
    return total
def main(vala, valh, people, room, sun):
    """main"""
    if vala <= 550:
        res = check1(vala)
    else:
        res = check2(vala)
    if valh > 8:
        res += (valh-8)*1000
    if people > 3:
        res += (people-2)*600
    if room == "kitchen":
        res += 4000
    res = res * check3(sun)
    print(int(res))
main(int(input()), int(input()), int(input()), input(), input())
