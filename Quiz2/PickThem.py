"""PickThem"""
def main():
    """main"""
    import json
    txt = input()
    new_txt = json.loads(txt)
    even = 0
    for i in new_txt:
        if i % 2 == 0:
            print(i)
            even = 1
    if even == 0:
        print("Nope")
main()
