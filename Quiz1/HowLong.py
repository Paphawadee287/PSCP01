"""HowLong"""
def _digits():
    """number of digits or length of digits"""
    number = int(input())
    digit = 0
    for _ in str(abs(number)):
        if str(number) != "-":
            digit += 1
    print(digit)
_digits()
