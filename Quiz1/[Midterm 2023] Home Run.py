"""[Midterm 2023] Home Run"""
def main(time, ans_vals):
    """main"""
    count = 0
    for _ in range(time):
        val_s = float(input())
        if ans_vals > val_s:
            count += 1
    print(count)
main(int(input()), float(input()))
