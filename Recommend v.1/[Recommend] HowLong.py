"""[Recommend] HowLong"""
def _digits():
    """number of digits or length of digits"""
    number = int(input())
    result = 0
    for _ in str(abs(number)):
        result += 1
    print(result)
_digits()
