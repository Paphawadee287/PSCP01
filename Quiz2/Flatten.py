"""Flatten"""
def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

my_list = input()
result = flatten_list(my_list)
print(result)

