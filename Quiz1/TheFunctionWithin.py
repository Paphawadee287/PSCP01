"""TheFunctionWithin"""
def val_f(val_a):
    """f(x)"""
    return 2 * val_a
def val_g(var_a):
    """g(x)"""
    return (3 * (var_a ** 4)) - (var_a ** 3) + (2 * (var_a ** 2)) + 10
def val_h(var_a, var_b, var_c):
    """h(x)"""
    return ((var_c + var_a) ** 2) - (var_a * var_b) + (var_b ** 2)
def val_i(var_a, var_b, var_c, var_d):
    """i(x)"""
    return ((var_a ** 2) + (var_b ** 2) - var_c ** 2) / \
        ((var_d ** 2) - (2 * var_a * var_d) + (2 * var_a))

def main(var_a, var_b, var_c, var_d):
    """main"""
    print(val_f(val_f(var_a)))
    print(val_g(val_f(var_a - var_b)))
    print(val_h(val_f(var_a + var_b), val_f(var_a + var_c), \
        val_g(val_f(var_d ** 2))))
    print(val_i(val_h(val_f(var_a + var_b), val_f(var_a - var_c), \
        val_g(val_f(var_d ** 2))), val_g(val_f(var_a - var_b)), \
        val_f(val_f(val_f(val_f(val_f(var_c))))), var_d ** 8))

main(float(input()), float(input()), float(input()), float(input()))
