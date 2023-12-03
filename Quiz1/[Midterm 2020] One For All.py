"""[Midterm 2020] One For All"""
def main(time):
    """main"""
    message = ""
    for i in range(1, time + 1):
        txt = input()
        if i == time:
            message += txt + "_%d" %i
        elif i % 2 == 0:
            message += txt + "-" * i
        else:
            message += txt + "*" * i
    print(message)
main(int(input()))
