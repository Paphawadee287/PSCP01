"""Divide3Or5"""
def main(val_n):
    """main"""
    count = 0
    for i in range(1, val_n + 1):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    print(count)
main(int(input()))
