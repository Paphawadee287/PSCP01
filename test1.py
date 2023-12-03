# def illuminatinum(num):
#     illulist = [333, 666, 777, 888]
#     if num % 3 == 0:
#         print("It's maybe Illuminati")
#     elif num % 13 == 0:
#         print("It's could be Illuminati")
#     if num == 3 or num == 13:
#         print("Illuminati Confirm")
#     elif num in illulist:
#         print("Illuminati Confirm!!!")
#     else:
#         print("It's not illuminati")
# illuminatinum(int(input()))
# list1 = [8, 7, 6, 5, 4, 3, 2, 1]
# list2 = sorted(list1)
# print(list2)
# print(list1)
# def create_hello_frame():
#     """create frame"""
#     count = 0
#     txt = ""
#     for _ in range(5):
#         message = input()
#         if count < len(message):
#             count = len(message)
#         txt += message + "\n"
#     frame_width = count + 4  # 4 เป็นจำนวนช่องว่างรอบข้อความ
#     frame = "*" * frame_width  # สร้างบรรทัดบนสุด
#     frame += "\n* {} *".format(txt)  # สร้างบรรทัดข้อความ
#     frame += "\n" + "*" * frame_width  # สร้างบรรทัดล่างสุด
#     print(frame)

# create_hello_frame()
# x = "Hello World       "
# print(len(x))
# y = x.strip(" ")
# print(len(y))
# number01 = 12
# number02 = 20

# num1Or = number01  
# num2Or = number02

# def resetVar():
#     global number01, number02
#     number01 = num1Or
#     number02 = num2Or

# number01 += 1  
# number02 += 2  

# print(number01) 
# print(number02) 

# resetVar() 

# print(number01)
# print(number02) 
# res = 0
# while True:
#     num = input()
#     if num == "ENTER":
#         break
#     res += int(num)
# print(res-50-50-55-55)

# def main(valx, valy, money, valz):
#     """main"""
#     people = (valz // valx) + valy
#     print(people*money)
# main(int(input()), int(input()), int(input()), int(input()))

res = []
while True:
    txt = input()
    if txt == "yo":
        break
    elif txt == "kkk":
        res.append(txt[0])
    else:
        res.append(txt)
print(res)