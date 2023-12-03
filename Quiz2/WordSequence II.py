"""WordSequence II"""
def main(txt, change):
    """main"""
    for i in range(max(len(txt), len(change))+1):
        print(change[:i] + txt[i:])
main(input(), input())
