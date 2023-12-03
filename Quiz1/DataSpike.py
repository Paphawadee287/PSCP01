"""DataSpike"""
def find_most(data, highest):
    """find highest"""
    if  data > highest:
        return data
    return highest

def main(count, highest=0):
    """main"""
    if count >= 1:
        data = int(input())
        highest = find_most(data, highest)
        if count == 1:
            print(highest)
        main(count - 1, highest)
main(8)
