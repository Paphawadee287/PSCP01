"""MissingCard (No Set)"""
def main():
    """main"""
    rank1 = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    rank2 = ['S', 'H', 'D', 'C']
    all_card = []
    mycard = []
    for i in rank1:
        for j in rank2:
            all_card.append(i+j)
    for _ in range(51):
        card = input()
        mycard.append(card)
    for i in all_card:
        if i not in mycard:
            print(i)
            break
main()
