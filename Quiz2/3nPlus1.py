"""3nPlus1"""
def main():
    """main"""
    while True:
        nums = int(input())
        if nums == 0:
            break
        count = 1
        while nums != 1:
            if nums % 2 == 0:
                nums /= 2
            else:
                nums = (nums * 3) + 1
            count += 1
        print(count)
main()
