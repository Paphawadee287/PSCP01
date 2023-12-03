"""Align"""
def main():
    """main"""
    size = int(input())
    position = input()
    txt = input()
    if position == 'left':
        print(txt.ljust(size))
    elif position == 'center':
        if len(txt) % 2 != 0:
            print('', txt.center(size - 1))
        else:
            print(txt.center(size))
    else:
        print(txt.rjust(size))
main()
