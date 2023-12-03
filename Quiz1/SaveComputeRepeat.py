"""SaveComputeRepeat"""
def time():
    """days hours minutes seconds milliseconds"""
    start_here = 267009000
    milliseconds = start_here
    seconds = milliseconds // 1000
    milliseconds %= 1000
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    print(days, hours, minutes, seconds, milliseconds)
time()
