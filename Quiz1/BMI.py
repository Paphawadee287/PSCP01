"""BMI"""
def cal_bmi(name, weight, tall, i):
    """find BMI"""
    bmi = weight / ((tall / 100) ** 2)
    print(name + "'s  BMI =", "%.2f" %bmi)
    input_data(i + 1)

def input_data(i=1):
    """main"""
    if i < 6:
        name = input()
        weight = float(input())
        tall = float(input())
        cal_bmi(name, weight, tall, i)
input_data()

"""
def main(count):
    if count < 5:
        name = str(input())
        weight = float(input())
        height = float(input())
        result = (weight/((height/100)**2))
        print(name+"'s ", "BMI =", "%.2f" %result)
        main(count+1)
main(0)
"""