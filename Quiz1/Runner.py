"""Runner"""
def runner():
    """returns k lines of text"""
    txt = input()
    number = int(input())
    for _ in range(number):
        print(txt)
runner()
