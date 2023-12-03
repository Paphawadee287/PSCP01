"""FibonacciRecursionV1"""
def fibonacci(val, vala=0, valb=1, counter=0):
    """fibonacci"""
    if counter == val:
        return vala
    else:
        return fibonacci(val, valb, vala + valb, counter + 1)

print(fibonacci(int(input())))
