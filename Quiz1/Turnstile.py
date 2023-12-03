"""Turnstile"""
def main():
    """main"""
    count = 0
    nub = False
    while True:
        txt = input()
        if txt == 'END':
            break
        if txt == 'C':
            nub = True
        elif txt == 'P' and nub:
            count += 1
            nub = False
    print(count)
main()
