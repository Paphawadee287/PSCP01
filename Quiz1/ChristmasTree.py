"""ChristmasTree"""
def main():
    """main"""
    leave = int(input())
    tree = int(input())
    for i in range(leave):
        print(' ' * (leave - i - 1) + '*' * (2 * i + 1))
    for _ in range(tree):
        print(' ' * (leave - 2) + '-' * 3)
main()
