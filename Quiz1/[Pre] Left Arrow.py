"""[Pre] Left Arrow"""
def main():
    """main"""
    wide = int(input())
    high = int(input())
    for i in range(high):
        if i <= high // 2:
            print(' ' * ((high // 2) - i) + '*' * wide)
        else:
            print(' ' * (-1 * ((high // 2) - i)) + '*' * wide)
main()
