"""Day I"""
def years_29(year):
    """find a years with 29 days"""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def main():
    """main"""
    year = int(input())
    if years_29(year) == True:
        print("Yes")
    else:
        print("No")
main()
