"""
หลัก PEP-8 & ข้อผิดพลาดอื่น ๆ
    ข้อผิดพลาด
    1. Missing Doc
    2. Missing Newline
    3. Line to long แก้โดยใส่  \
    4. Bad white space มีช่องว่างข้างหลังให้ใส่ !
    5. Missing tab and white space

    6. variables name error
    7. Too many branches การใช้ statement if-else มากไป/
       มี loop มากกว่า 12 ครั้งใน 1 function

หลักตั้งชื่อ
    1.พิมพ์เล็ก
    2.ไม่ขึ้นต้นด้วยเลข
    3.ไม่สั้น ไม่ยาวเกินไป (ต้องมี 3 ตัวอักษรขึ้นไป)

    การเกิด error
    1. Syntax error เขียนผิดรูปแบบของภาษา
    2. Type error เช่น
        txt = "2"
        print(txt / 2) Error  string / int
    3. Value error ใส่ argument ที่ไม่สามารแปลงค่าได้ เช่น แปลง "X"(string) => int
    4. Name error เรียกใช้ตัวแปรที่ยังไม่ได้ประกาศก่อนหน้า
    5. Zero devision error 10 / 0

ชนิดข้อมูล
    String Float Integer Boolean
    อื่น ๆ Tuple => ('F', "Hello", 1234) List => [1, 2, 3]

Python print argument
    1. comma
    2. sep="" เช่น
        print("Hello", "World", "123", sep="---")
        Hello---World---123
    3. end="" เช่น
        print("Hello", "World", "123", end="---")
        Hello World 123---

Formatting
    string formatting %s %d %f

Escape character
    (\') '
    (\") "
    (\\) \
    (\n) บรรทัดใหม่
    
Operators


"""
# การเรียกใช้ function
