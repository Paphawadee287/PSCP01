"""[Recommended] ATM"""
def main(money):
    """main"""
    while True:
        menu = input().split()
        if 'END' in menu:
            break
        if menu[0] == 'D':
            money += int(menu[1])
        else:
            if money - int(menu[1]) >= 0:
                money -= int(menu[1])
            else:
                money = 0
    print(money)
main(int(input()))
