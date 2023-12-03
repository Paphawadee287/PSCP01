"""Inverter"""
def main(bits):
    """main"""
    res = ""
    for i in bits:
        if i == "0":
            res += "1"
        else:
            res += "0"
    for i, j in enumerate(res, start=0):
        if j == "1":
            print(res[i:])
            break
main(input())
