"""Jumping"""
def print_output(i, txt):
    """main"""
    if i < 4:
        print(txt)
        print_output(i + 1, txt)
        return

def jumping():
    """main"""
    print_output(1, "Output1")
    print_output(1, "Output2")
    print_output(1, "Output3")
    print_output(1, "Output4")
jumping()

"""
def jumping():
    print_output(1)
    print_output(2)
    print_output(3)
    print_output(4)
def print_output(num):
    print("Output" + str(num))
    print("Output" + str(num))
    print("Output" + str(num))
jumping()
"""