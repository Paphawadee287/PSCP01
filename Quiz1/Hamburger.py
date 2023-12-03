"""Hamburger"""
def main():
    """main"""
    left = int(input())
    right = int(input())
    meat = (left + right) * 2
    print(("|" * left) + "*" * meat + ("|" * right))
main()
