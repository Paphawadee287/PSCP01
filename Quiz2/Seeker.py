"""Seeker"""
import re
def main(txt):
    """main"""
    summ = 0
    ans = re.findall(r"\d+", txt)
    for i in ans:
        summ += int(i)
    print(summ)
main(input())
