"""MissingCard I"""
def main():
    """main"""
    rank1 = {'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'}
    rank2 = {'S', 'H', 'D', 'C'}
    all_card = set()
    mycard = set()
    for i in rank1:
        for j in rank2:
            all_card.add(i+j)
    for _ in range(51):
        card = input()
        mycard.add(card)
    missing = all_card.difference(mycard)
    print(*missing)
main()
