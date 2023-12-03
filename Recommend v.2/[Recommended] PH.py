"""[Recommended] PH"""
def main(valph):
    """main"""
    if 0 <= valph <= 14:
        if valph < 7:
            print("acidic")
        elif valph == 7:
            print("neutral")
        else:
            print("akaline")
    else:
        print("error")

main(float(input()))
