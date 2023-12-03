"""[Recommend] RuleofThree"""
def main(time):
    """main"""
    for _ in range(time):
        price = float(input())
        size = float(input())
        ans = price / size

main(int(input()))
