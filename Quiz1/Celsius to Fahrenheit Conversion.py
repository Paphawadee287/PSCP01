"""Celsius to Fahrenheit Conversion"""
def celsius():
    """fahrenheit >> celsius"""
    var_f = float(input())
    result_c = (var_f - 32) / 9 * 5
    print("%.1f" %result_c, "Celsius")
celsius()
