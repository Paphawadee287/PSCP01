"""Diamond I"""
def main(val_h, val_w):
    """main"""
    value = []
    count = 0
    res = 0
    for _ in range(val_h):
        num = input().split(" ")
        value.append(num)
    for number, i in enumerate(value, 0):
        if count == val_h:
            number += 1
            continue
        res += int(i[number])
    print(res)
        
main(int(input()), int(input()))