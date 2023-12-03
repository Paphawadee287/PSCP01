"""BloodDonation"""
def check_17(book):
    """check"""
    if book == "True":
        return "Yes"
    return "No"

def check_60(num, book):
    """check"""
    if book == "True" and num != 0:
        return "Yes"
    return "No"

def check(age, num):
    """check"""
    if age >= 55 and num == 0:
        return "No"
    return "Yes"

def main(age, weight, num):
    """main"""
    if 17 <= age <= 70 and weight >= 45:
        if age == 17:
            book = input()
            print(check_17(book))
        elif 60 <= age <= 70:
            book = input()
            print(check_60(num, book))
        else:
            print(check(age, num))
    else:
        print("No")
main(int(input()), int(input()), int(input()))
