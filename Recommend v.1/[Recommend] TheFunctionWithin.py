"""[Recommend] TheFunctionWithin"""
def func_f(val_x):
    """f(x)"""
    return 2 * val_x
def func_g(val_x):
    """g(x)"""
    return (3 * (val_x ** 4)) - (val_x ** 3) + (2 * (val_x ** 2)) + 10
def func_h(val_x, val_y, val_z):
    """h(x, y, z)"""
    return ((val_z + val_x) ** 2) - (val_x * val_y) + (val_y ** 2)
def func_i(val_a, val_b, val_c, val_d):
    """i(a, b, c, d)"""
    return ((val_a ** 2) + (val_b ** 2) - (val_c ** 2)) / ((val_d ** 2) - \
            (2 * val_a * val_d) + (2 * val_a))

def main(val_a, val_b, val_c, val_d):
    """main"""
    print(func_f(func_f(val_a)))
    print(func_g(func_f(val_a - val_b)))
    print(func_h(func_f(val_a + val_b), func_f(val_a + val_c), func_g(func_f(val_d ** 2))))
    print(func_i(func_h(func_f(val_a + val_b), func_f(val_a - val_c), func_g(func_f(val_d ** 2))), \
            func_g(func_f(val_a - val_b)), func_f(func_f(func_f(func_f(func_f(val_c))))), \
            val_d ** 8))
main(float(input()), float(input()), float(input()), float(input()))
