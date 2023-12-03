"""FoodGrade I"""
def wing(number):
    """cal wing"""
    if number >= 50 and number <= 70:
        return 1
    else:
        return 0

def main(number, count=0):
    """input"""
    if number >= 1:
        weight = float(input())
        answer = wing(weight)
        if answer == 1:
            count += 1
        if number == 1:
            print(count)
        main(number - 1, count)

main(24)
