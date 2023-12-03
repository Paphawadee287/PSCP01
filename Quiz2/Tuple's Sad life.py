"""Tuple's Sad life"""
def main(number, find):
    """main"""
    number_tup = tuple(number.split(' '))
    num_index = number_tup.index(find)
    find_count = number_tup.count(find)
    for _ in range(find_count):
        res = ""
        for _ in range(find_count):
            res += str(num_index) + " "
        print(res)
main(input(), input())
