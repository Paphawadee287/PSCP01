"""[Midterm 2020] Shorten"""
def main(f_num):
    """main"""
    l_num = 0
    result = ""
    while True:
        number = int(input())
        if number == -1:
            if result == "":
                result = "%d-%d" %(f_num, l_num)
            print(result)
            break
        if f_num + 1 != number and l_num + 1 != number:
            if l_num == 0:
                result += "%d, " %f_num
            else:
                result += "%d-%d, " %(f_num, l_num)
            f_num = number
            l_num = 0
        else:
            l_num = number
main(int(input()))
