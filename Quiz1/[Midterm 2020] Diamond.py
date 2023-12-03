"""[Midterm 2020] Diamond"""
def main(length):
    """main"""
    mid = length // 2
    count = 2
    for i in range(length):
        if i == mid:
            print('*' * length)
            continue
        if i > mid:
            i -= count
            count += 2
        for j in range(length):
            if (j == mid + i or j == mid - i) or i == length:
                print('*', end="")
            else:
                print(' ', end="")
        print()
main(int(input()))
