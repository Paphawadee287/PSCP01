"""Nearer"""
def main():
    """main"""
    alice = int(input())
    bob = int(input())
    car = int(input())
    coordinates_a = abs(car - alice)
    coordinates_b = abs(car - bob)
    if coordinates_a < coordinates_b:
        print("Alice %d" %coordinates_a)
    elif coordinates_a > coordinates_b:
        print("Bob %d" %coordinates_b)
    else:
        print("Sundaes %d" %coordinates_a)
main()
