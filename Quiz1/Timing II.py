"""Timing II"""
def time():
    """days hours minutes seconds"""
    all_seconds = int(input())
    ans_seconds = all_seconds % 60
    seconds = all_seconds // 60
    ans_minutes = seconds % 60
    minutes = seconds // 60
    ans_hours = minutes % 24
    hours = minutes // 24
    ans_days = hours
    if len(str(ans_days)) <= 4:
        print("%04d" %ans_days, "%02d" %ans_hours, \
            "%02d" %ans_minutes, "%02d" %ans_seconds, sep=":")
    else:
        print("ERR_:__:__:__")
time()
