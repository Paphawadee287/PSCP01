"""Rectangle"""
def area(height, width):
    """cal area"""
    print(int(height * width))
def circumference(height, width):
    """cal circumference"""
    print(int(2 * (height + width)))
def cal_square(height, width):
    """area and circumference"""
    area(height, width)
    circumference(height, width)
cal_square(float(input()), float(input()))
