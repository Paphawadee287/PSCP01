"""[Pre] Blackjack"""
def main():
    """
    ไพ่ 2 ใบ รวมกัน ไม่เกิน 21
    ace มีค่า 1 , 11
    """
    time = int(input())
    result = 0
    for _ in range(time):
        card = input()
        if card.isdigit():
            result += int(card)
        elif card == "A":
            if result + 11 > 21:
                result += 1
            else:
                result += 11
        else:
            result += 10
    print(result)
main()