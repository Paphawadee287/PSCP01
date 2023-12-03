"""LastStand"""
def main():
    """main"""
    import json
    txt = input()
    number = json.loads(txt)
    for i in number:
        print(str(i)[-1:])
main()
