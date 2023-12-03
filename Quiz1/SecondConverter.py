"""SecondConverter"""
def main(val_k, val_s, val_m, val_h):
    """main"""
    ans_seconds = val_k % val_s
    sec = val_k // val_s
    ans_mins = sec % val_m
    minutes = sec // val_m
    ans_hours = minutes % val_h
    print("%d:%d:%d" %(ans_hours, ans_mins, ans_seconds))
main(int(input()), int(input()), int(input()), int(input()))
