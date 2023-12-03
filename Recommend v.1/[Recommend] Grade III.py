"""[Recommend] Grade III"""
def check(grade):
    """check grade"""
    import math
    if 95 <= grade <= 100:
        return 4.00
    elif 90 <= grade < 95:
        if grade >= math.ceil((90 + 95) / 2):
            return 3.75
        return 3.50
    elif 85 <= grade < 90:
        if grade >= math.ceil((85 + 90) / 2):
            return 3.25
        return 3.00
    elif 80 <= grade < 85:
        if grade >= math.ceil((80 + 85) / 2):
            return 2.75
        return 2.50
    elif 75 <= grade < 80:
        if grade >= math.ceil((75 + 80) / 2):
            return 2.25
        return 2.00
    elif 70 <= grade < 75:
        if grade >= math.ceil((70 + 75) / 2):
            return 1.75
        return 1.50
    elif 65 <= grade < 70:
        if grade >= math.ceil((65 + 70) / 2):
            return 1.25
        return 1.00
    elif 60 <= grade < 65:
        if grade >= math.ceil((60 + 65) / 2):
            return 0.75
        return 0.50
    elif 0 <= grade < 60:
        if grade >= math.ceil((0 + 60) / 2):
            return 0.25
        return 0
def main():
    """main"""
    time = int(input())
    total_score = 0
    for _ in range(time):
        score = float(input())
        total_score += score
    grade = total_score // time
    print(check(grade))
main()
