"""iPad Air"""
def main():
    """iPad Air"""
    colour = input().lower()
    storage = input()
    port = input()
    price = 0
    if colour in ("space gray", "silver", "green", "rose gold", "sky blue"):
        if storage in ("64", "256"):
            if port == "Wi-Fi" and storage == "64":
                price = 19900
                print(price)
            elif port == "Wi-Fi" and storage == "256":
                price = 24900
                print(price)
            elif port == "Wi-Fi + Cellular" and storage == "64":
                price = 24400
                print(price)
            elif port == "Wi-Fi + Cellular" and storage == "256":
                price = 29400
                print(price)
            else:
                print("Not Available")
        else:
            print("Not Available")
    else:
        print("Not Available")
main()
