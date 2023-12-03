"""Timing"""
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
    print(ans_days, ans_hours, ans_minutes, ans_seconds)
time()
