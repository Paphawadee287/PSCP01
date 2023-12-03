"""[Midterm 2020] BTSMRT"""
def main():
    """
    child < 14, <= 140 free
    seni >= 60 free
    normal pay
    < 14, < 90 free
    """
    days = input()
    age = float(input())
    high = float(input())
    result = "PAY"
    if age < 14 and high < 90:
        result = "FREE"
    if days == "Children Day" and age < 14 and high <= 140:
        result = "FREE"
    if days == "Senior Day" and age >= 60:
        result = "FREE"
    print(result)
main()
