"""Hamming"""
def main(txt1, txt2):
    """main"""
    count = 0
    for i in range(len(txt1)):
        if txt1[i] != txt2[i]:
            count += 1
    print(count)
main(input(), input())
