"""Run Length Decoding"""
def main(txt):
    """main"""
    number = ""
    result = ""
    for i in txt:
        if i.isdigit():
            number += i
        elif i.islower():
            result += i * int(number)
            number = ""
    print(result)
main(input())
