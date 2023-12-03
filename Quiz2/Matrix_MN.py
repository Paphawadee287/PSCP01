"""Matrix_MN"""
def main():
    "Matrix_MN"
    matrixm = int(input())
    matrixn = int(input())
    res = ""
    for _ in range(matrixm):
        for _ in range(matrixn):
            res += input() + " "
        print(res)
        res = ""
main()
