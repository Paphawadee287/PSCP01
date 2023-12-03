"""[Recommend] SumOfNumber"""
def sum_number():
    """sum of number"""
    goal = int(input())
    result = 0
    while result != goal:
        number = int(input())
        if number == -1:
            break
        result += number
    print(result)
sum_number()
