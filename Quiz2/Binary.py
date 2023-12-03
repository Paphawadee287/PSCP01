"""Binary"""
def main(number):
    """main"""
    res = ""
    while number:
        if number%2 == 0:
            res += '0'
        else:
            res += '1'
        number //= 2
    res = print(0) if res == "" else print(res[::-1])
main(int(input()))
