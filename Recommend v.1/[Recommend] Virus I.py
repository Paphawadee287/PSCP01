"""[Recommend] Virus I"""
def virus():
    """virus"""
    txt = input()
    total = 0
    for i in txt:
        if i == 'o':
            total += 1
    print(total)
virus()
