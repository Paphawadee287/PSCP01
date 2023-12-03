"""[Recommended] Music Lover"""
def main(num):
    """main"""
    singer = {}
    for _ in range(num):
        entry = input().split("-")
        if entry[0] in singer:
            singer[entry[0]].append(entry[1])
        else:
            singer[entry[0]] = [entry[1]]
    for i in singer.keys():
        print(i)
        for j in singer[i]:
            print(j)
main(int(input()))
