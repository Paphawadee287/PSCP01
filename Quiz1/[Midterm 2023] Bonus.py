"""[Midterm 2023] Bonus"""
def main(salary, years, months):
    """main"""
    if months >= 10:
        years += 1
    total_years = min(years, 20)
    all_salary = total_years * salary
    total_salary = min(max(all_salary, 5000), 1000000)
    print(total_salary)
main(int(input()), int(input()), int(input()))
