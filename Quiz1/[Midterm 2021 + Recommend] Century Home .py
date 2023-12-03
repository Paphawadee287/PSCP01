"""[Midterm 2021 + Recommend] Century Home """
def main(time):
    """main"""
    import math
    for _ in range(time):
        txt = input()
        number = ""
        for j in txt:
            if j.isdigit():
                number += j
        if "B.E." in txt:
            result = math.ceil((int(number) - 543) / 100)
        elif "A.D." in txt:
            result = math.ceil(int(number) / 100)
        if result > 0:
            print(result)
        else:
            print("ERROR")
main(int(input()))
