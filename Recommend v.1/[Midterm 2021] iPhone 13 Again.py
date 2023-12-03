"""[Midterm 2021] iPhone 13 Again"""
def iphone_13_mini(capacity):
    """check"""
    if capacity == "128 GB":
        return "25900"
    elif capacity == "256 GB":
        return "29900"
    elif capacity == "512 GB":
        return "37900"
    return "Not Available"
def iphone_13(capacity):
    """check"""
    if capacity == "128 GB":
        return "29900"
    elif capacity == "256 GB":
        return "33900"
    elif capacity == "512 GB":
        return "41900"
    return "Not Available"
def iphone_13_pro(capacity):
    """check"""
    if capacity == "128 GB":
        return "38900"
    elif capacity == "256 GB":
        return "42900"
    elif capacity == "512 GB":
        return "50900"
    elif capacity == "1 TB":
        return "58900"
    return "Not Available"
def iphone_13_pro_max(capacity):
    """check"""
    if capacity == "128 GB":
        return "42900"
    elif capacity == "256 GB":
        return "46900"
    elif capacity == "512 GB":
        return "54900"
    elif capacity == "1 TB":
        return "62900"
    return "Not Available"
def iphone(gen, capacity):
    """gen"""
    if gen == "iPhone 13 mini":
        print(iphone_13_mini(capacity))
    elif gen == "iPhone 13":
        print(iphone_13(capacity))
    elif gen == "iPhone 13 Pro":
        print(iphone_13_pro(capacity))
    elif gen == "iPhone 13 Pro Max":
        print(iphone_13_pro_max(capacity))
    else:
        print("Not Available")

iphone(input(), input())
