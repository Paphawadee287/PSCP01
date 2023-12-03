"""FizzBuzz"""
def main():
    """main"""
    number = int(input())
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            ans = "FizzBuzz"
        elif i % 3 == 0:
            ans = "Fizz"
        elif i % 5 == 0:
            ans = "Buzz"
        else:
            ans = i
        print(ans)
main()
