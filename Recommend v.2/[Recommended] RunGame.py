"""[Recommended] RunGame"""
def main(valk):
    """main"""
    count = int(valk[0])
    for i in range(1, len(valk)):
        print(i)
        count += abs(int(valk[i-1]) - int(valk[i]))
        print(count)
main(input().split(" "))
