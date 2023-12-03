"""Right Arrow"""
def main(wide, high):
    """main"""
    for i in range(high):
        if i <= high // 2:
            print(' ' * i + '*' * wide)
        else:
            print(' ' * (high - i - 1) + '*' * wide)
main(int(input()), int(input()))
