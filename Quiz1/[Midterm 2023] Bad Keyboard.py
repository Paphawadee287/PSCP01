"""[Midterm 2023] Bad Keyboard"""
def main(txt):
    """main"""
    message = ""
    for i in txt:
        if i == 'i':
            i = 'o'
        elif i == 'o':
            i = 'i'
        elif i == 'I':
            i = 'O'
        elif i == 'O':
            i = 'I'
        message += i
    print(message)
main(input())
