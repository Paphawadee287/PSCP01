"""Boomerang"""
def main():
    """main"""
    valx = int(input())
    valy = int(input())
    valz = int(input())
    print(valx + 1)
    print((7 * valy ** 3) + (2 * valy ** 2) - (31 * valy) + 1)
    print(-valz)
    print((valx + valy) * (valx - valy))
    print((valy - ((valy ** 2 - (4 * valx * valz)) ** 0.5)) / (2 * valx))
main()
