"""[Midterm 2023] Password"""
def main(password):
    """main"""
    for i in password:
        if i.isupper():
            print(True)
            break
main(input())