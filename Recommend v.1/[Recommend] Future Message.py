"""[Recommend] Future Message"""
def message():
    """message"""
    txt = input()
    if txt.isdigit():
        print("Number")
    elif txt.isspace():
        print("Space")
    elif txt.isupper():
        print("Uppercase")
    elif txt.islower():
        print("Lowercase")
    elif txt.istitle():
        print("Title")
    else:
        print("Other")
message()
