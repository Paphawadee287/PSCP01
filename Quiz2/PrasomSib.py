"""PrasomSib"""
def main(num):
    """main"""
    count = 0
    ans = 0
    for i in range(len(num)):
        for j in range(len(num)):
            count = int(num[i]) + int(num[j])
            if count == 10:
                ans += 1
                break
            elif count > 10:
                count = int(num[j])
    print(ans)
main(input())
