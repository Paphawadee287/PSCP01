"""[Recommended] Area"""
def main(num):
    """main"""
    count = 0
    for _ in range(num):
        nub = input().replace(" ", "")
        count += len(nub)
    print(count)
main(int(input()))
