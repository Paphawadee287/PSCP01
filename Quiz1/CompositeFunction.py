"""CompositeFunction"""
def func_f(val_x):
    """fine f(x)"""
    return 2 * val_x

def func_g(val_x):
    """fine g(x)"""
    return val_x / 2 + 1

def function(val_x):
    """main"""
    print("%.2f" %func_f(func_g(val_x)))
    print("%.2f" %func_g(func_f(val_x)))
function(int(input()))
