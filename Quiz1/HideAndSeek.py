"""HideAndSeek"""
def main():
    """main"""
    start = int(input())
    stop = int(input())
    step = int(input())
    for i in range(start, stop, step):
        print(i)
main()
