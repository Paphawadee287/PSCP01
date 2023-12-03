"""PongYa"""
def main(num):
    "PongYa"
    res = ""
    for i in range(1, num+1):
        if num%3 == 0:
            res = "PONG"
        elif str(num)[-1] == "3":
            res = "PONG"
        else:
            res = str(i)
    print(res)
main(int(input()))
