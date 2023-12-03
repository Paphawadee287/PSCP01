"""Virus I"""
def main():
    """main"""
    virus = input()
    count = 0
    for i in virus:
        if i == 'o':
            count += 1
    print(count)
main()
